
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes

from array import array
import os
from PIL import Image
import sys
import time
import http.client, urllib.request, urllib.parse, urllib.error, base64



def DenseCaptioning(imgPath):
    key = '2d3cb8d128e34b73b9e0a49b810449ee'
    endpoint = "https://ywu4.cognitiveservices.azure.com/"
    creds = CognitiveServicesCredentials(key)
    client = ComputerVisionClient(endpoint, creds)
    with open(imgPath, 'rb') as img:
        result = client.analyze_image_in_stream(img, [VisualFeatureTypes.adult,
                                                            VisualFeatureTypes.brands,
                                                            VisualFeatureTypes.categories,
                                                            VisualFeatureTypes.color,
                                                            VisualFeatureTypes.description,
                                                            VisualFeatureTypes.faces,
                                                            VisualFeatureTypes.image_type,
                                                            VisualFeatureTypes.objects,
                                                            VisualFeatureTypes.tags])
    tags = result.tags
    adult = result.adult
    brands = result.brands
    categories = result.categories
    color = result.color
    description = result.description
    faces = result.faces
    image_type = result.image_type
    objects = result.objects
    readable_res = "Image Tags:\n"
    for tag in tags:
        readable_res += f"- {tag.name} (confidence: {tag.confidence})\n"
    
    readable_res += "\nAdult Content:\n"
    readable_res += f"- Is Adult Content? {adult.is_adult_content}\n"
    readable_res += f"- Adult Score: {adult.adult_score}\n"
    readable_res += f"- Is Racy Content? {adult.is_racy_content}\n"
    readable_res += f"- Racy Score: {adult.racy_score}\n"

    if len(brands) > 0:
        readable_res += "\nBrands:\n"
        for brand in brands:
            readable_res += f"- {brand.name} (confidence: {brand.confidence})\n"
    
    readable_res += "\nCategories:\n"
    for category in categories:
        readable_res += f"- {category.name} (confidence: {category.score})\n"

    readable_res += "\nDominant Color:\n"
    readable_res += f"- Background Color: {color.dominant_color_background}\n"
    readable_res += f"- Foreground Color: {color.dominant_color_foreground}\n"
    readable_res += f"- Accent Color: {color.accent_color}\n"
    
    if len(description.captions) > 0:
        readable_res += "\nImage Description:\n"
        for caption in description.captions:
            readable_res += f"- {caption.text} (confidence: {caption.confidence})\n"
    
    if len(faces) > 0:
        readable_res += "\nFaces:\n"
        for face in faces:
            readable_res += f"- Gender: {face.gender}\n"
            readable_res += f"- Age: {face.age}\n"
            readable_res += f"- Emotion: {face.emotion}\n"
    
    if image_type.clip_art_type != 0:
        readable_res += "- Clip Art Detected\n"
    elif image_type.line_drawing_type != 0:
        readable_res += "- Line Drawing Detected\n"
    
    if len(objects) > 0:
        readable_res += "\nObjects:\n"
        for obj in objects:
            readable_res += f"- {obj.object_property} (confidence: {obj.confidence})\n"
    
    return(readable_res)
    # do something
    '''
    Authenticate
    Authenticates your credentials and creates a client.
    '''
    subscription_key = os.environ["subscriptionKeyAzure"]

    computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))    # do something
    '''
    Authenticate
    Authenticates your credentials and creates a client.
    '''
    subscription_key = os.environ["subscriptionKeyAzure"]

    computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
    '''
    END - Authenticate
    '''

    '''
    OCR: Read File using the Read API, extract text - remote
    This example will extract text in an image, then print results, line by line.
    This API call can also extract handwriting style text (not shown).
    '''
    print("===== Read File - remote =====")
    # # Get an image with text
    # read_image_url = "https://raw.githubusercontent.com/MicrosoftDocs/azure-docs/master/articles/cognitive-services/Computer-vision/Images/readsample.jpg"

    # # Call API with URL and raw response (allows you to get the operation location)
    # read_response = computervision_client.read(read_image_url,  raw=True)

    # Read local image file
    read_image_path = imgPath

    # Call API with local file path and raw response (allows you to get the operation location)
    with open(read_image_path, "rb") as image_stream:
        read_response = computervision_client.read_in_stream(image_stream,  raw=True)

    # Get the operation location (URL with an ID at the end) from the response
    read_operation_location = read_response.headers["Operation-Location"]
    # Grab the ID from the URL
    operation_id = read_operation_location.split("/")[-1]

    # Call the "GET" API and wait for it to retrieve the results 
    while True:
        read_result = computervision_client.get_read_result(operation_id)
        if read_result.status not in ['notStarted', 'running']:
            break
        time.sleep(1)

    # Print the detected text, line by line
    if read_result.status == OperationStatusCodes.succeeded:
        for text_result in read_result.analyze_result.read_results:
            for line in text_result.lines:
                print(line.text)
                print(line.bounding_box)
    print()
    '''
    END - Read File - remote
    '''

    print("End of Computer Vision quickstart.")


# result = DenseCaptioning("testocr.png")
# print(result)