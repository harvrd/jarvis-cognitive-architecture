import replicate
output = replicate.run(
    "pablodawson/segment-anything-automatic:14fbb04535964b3d0c7fad03bb4ed272130f15b956cbedb7b2f20b5b8a2dbaa0",
    input={"image": open("newestproj/cola.png", "rb")}
)
print(output)