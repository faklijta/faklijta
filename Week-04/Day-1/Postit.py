# Create a few example post-it objects:
# an orange with blue text: "Idea 1"
# a pink with black text: "Awesome"
# a yellow with green text: "Superb!"

class PostIt(object):
    background_color = ""
    text = ""
    text_color = ""

postit1 = PostIt()
postit2 = PostIt()
postit3 = PostIt()

postit1.background_color = "orange"
postit2.background_color = "pink"
postit3.background_color = "yellow"

postit1.text_color = "blue"
postit2.text_color = "black"
postit3.text_color = "green"

postit1.text = "Idea 1"
postit2.text = "Awsome"
postit3.text = "Superb"

print("post it 1 color is " + postit1.background_color + " text is " + postit1.text_color + " says: " + postit1.text)
print("post it 2 color is " + postit2.background_color + " text is " + postit2.text_color + " says: " + postit2.text)
print("post it 3 color is " + postit3.background_color + " text is " + postit3.text_color + " says: " + postit3.text)