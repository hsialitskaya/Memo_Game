def are_the_same(image1, image2):
    return image1 in image2 or image2 in image1

def test_are_the_same():
    assert are_the_same("cat1", "cat") == True
    assert are_the_same("dog", "cat") == False