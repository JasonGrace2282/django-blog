from config import RenderIfLoggedIn


class BlogView(RenderIfLoggedIn):
    main = 'blog.html'
