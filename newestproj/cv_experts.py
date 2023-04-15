from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from IPython.display import Image
import os


AZURE_KEY= os.environ["subscriptionKeyAzure"]
END_POINT = "https://jarvis-dense-captioning.cognitiveservices.azure.com/"

python
creds = CognitiveServicesCredentials(AZURE_KEY)
client = ComputerVisionClient(endpoint=END_POINT, credentials=creds)

with open(image_path, 'rb') as img:
#     result = client.describe_image_in_stream(img)
    result2 = result = client.analyze_image_in_stream(img, [VisualFeatureTypes.adult,
                                                            VisualFeatureTypes.brands,
                                                            VisualFeatureTypes.categories,
                                                            VisualFeatureTypes.color,
                                                            VisualFeatureTypes.description,
                                                            VisualFeatureTypes.faces,
                                                            VisualFeatureTypes.image_type,
                                                            VisualFeatureTypes.objects,
                                                            VisualFeatureTypes.tags])

print("Visual Features:")
if isinstance(result.adult, AdultInfo):
    print("- Adult Content:")
    print(f"  - Is Adult Content: {result.adult.is_adult_content}")
    print(f"  - Is Racy Content: {result.adult.is_racy_content}")
    print(f"  - Adult Score: {result.adult.adult_score}")
    print(f"  - Racy Score: {result.adult.racy_score}")
else:
    print("- Adult Content: None")

##----------Brand---------------
if isinstance(result.brands, list):
    print("- Brands:")
    for brand in result.brands:
        print(f"  - Name: {brand.name}")
        print(f"  - Confidence: {brand.confidence}")
else:
    print("- Brands: None")
##----------Brand---------------
if isinstance(result.categories, list):
    print("- Categories:")
    for category in result.categories:
        if isinstance(category, Category):
            print(f"  - Name: {category.name}")
            print(f"  - Score: {category.score}")
else:
    print("- Categories: None")
##----------Brand---------------

if isinstance(result.color, ColorInfo):
    print("- Dominant Colors:")
    for color in result.color.dominant_colors:
        print(f"  - {color}")
else:
    print("- Dominant Colors: None")

## ------------Description------------
print("- Description:")
print(f"  - Captions:")
for caption in result.description.captions:
    print(f"    - Text: {caption.text}")
    print(f"      Confidence: {caption.confidence}")
## ------------Description------------

if isinstance(result.image_type, ImageType):
    print("- Image Type:")
    print(f"  - Clip Art Type: {result.image_type.clip_art_type}")
    print(f"  - Line Drawing Type: {result.image_type.line_drawing_type}")
else:
    print("- Image Type: None")

if isinstance(result.objects, ObjectHierarchy):
    print("- Objects:")
    for obj in result.objects.objects:
        print(f"  - Object: {obj.object_property}")
        print(f"    Confidence: {obj.confidence}")
else:
    print("- Objects: None")

## ------------tag------------
if isinstance(result.tags, list):
    print("- Tags:")
    for tag in result.tags:
        print(f"  - Name: {tag.name}")
        print(f"  - Confidence: {tag.confidence}")
else:
    print("- Tags: None")
## ------------tag------------
Image(filename=image_path, width=120, height=120)
 