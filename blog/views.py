from django.shortcuts import render
from datetime import date
# Create your views here.

posts_list = [
    {
        "slug": "the-mountains",
        "image": "mountains.jpg",
        "author": "Pawel",
        "date": date(2021, 7, 15),
        "title": "Mountain hiking",
        "excerpt": "There is nothing better then high mountain climbing!",
        "content": """
            Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, 
            totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta 
            sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia 
            consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui 
            dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora 
            incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum
            exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex
        """
    },
    {
        "slug": "the-bikes",
        "image": "woods.jpg",
        "author": "Emi",
        "date": date(2022, 1, 15),
        "title": "Bike riding",
        "excerpt": "There is nothing better then bike riding!",
        "content": """
        But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and 
        I will give you a complete account of the system, and expound the actual teachings of the great explorer of 
        the truth, the master-builder of human happiness.

No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to 
pursue pleasure rationally encounter consequences that are extremely painful.

Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because 
occasionally
            """
    },
    {
        "slug": "nordic-walking",
        "image": "mountains.jpg",
        "author": "Monia",
        "date": date(2021, 12, 15),
        "title": "Nordic walking",
        "excerpt": "There is nothing better then nordic walking!",
        "content": """
            The quick, brown fox jumps over a lazy dog. DJs flock by when MTV ax quiz prog. Junk MTV quiz graced by 
            fox whelps. Bawds jog, flick quartz, vex nymphs.

Waltz, bad nymph, for quick jigs vex! Fox nymphs grab quick-jived waltz. Brick quiz whangs jumpy veldt fox. 
Bright vixens jump; dozy fowl quack.

Quick wafting zephyrs vex bold Jim. Quick zephyrs blow, vexing daft Jim. Sex-charged fop blew my junk TV quiz. 
How quickly daft jumping zebras vex. Two driven jocks help fax my big quiz. Quick, Baz, get my woven flax jodhpurs! 
"Now fax quiz Jack! " my brave
        """
    },
    {
        "slug": "swimming-with-the-waves",
        "image": "woods.jpg",
        "author": "Ola",
        "date": date(2020, 7, 15),
        "title": "Swimming with waves",
        "excerpt": "There is nothing better then swimming with waves!",
        "content": """
            Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, 
            there live the blind texts.

Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean.

A small river named Duden flows by their place and supplies it with the necessary
        """
    }
]


def get_date(post):
    return post["date"]


def index(request):
    sorted_list = sorted(posts_list, key=get_date)
    last_3_posts = sorted_list[-3:]

    return render(request, "blog/index.html", {
        "posts": last_3_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "posts": posts_list
    })


def post_detail(request, slug):
    found_post = next(post for post in posts_list if post["slug"] == slug)
    return render(request, "blog/post-detail.html", {
        "post" : found_post
    })

