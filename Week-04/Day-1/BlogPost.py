
class BlogPost(object):
    author_name = ""
    title = ""
    text = ""
    publication_date = ""


blogpost1 = BlogPost
blogpost2 = BlogPost
blogpost3 = BlogPost

blogpost1.author_name = "John Doe"
blogpost1.title = "Lorem ipsum"
blogpost1.publication_date = "2000.05.04."
blogpost1.text = "Lorem ipsum dolor sit amet"

blogpost2.author_name = "Tim Urban"
blogpost2.title = "Wait but why"
blogpost2.publication_date = "2010.10.10."
blogpost2.text = "A popular long-form, stick-figure-illustrated blog about almost everything"

blogpost2.author_name = "William Turton"
blogpost2.title = "One Engineer Is Trying to Get IBM to Reckon With Trump"
blogpost2.publication_date = "2017.03.28."
blogpost2.text = "Daniel Hanley, a cybersecurity engineer at IBM, doesn’t want to be the center of attention. When I asked to take his picture outside one of IBM’s New York City offices, he told me that he wasn’t really into the whole organizer profile thing."
