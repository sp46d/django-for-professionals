from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView

# What to test in unittest for pages app:
# - we need to test our urls:
#   1. if urls exist at correct locations, 
#   2. if urls have correct names that we set, 
#   3. if urls use correct templates (i.e. html), 
#   4. if urls render html that has correct contents
# - we need to test our views:
#   1. if view functions resolve correct urls (i.e. if views are associated with correct urls)

class HomePageTests(SimpleTestCase):
    def setUp(self) -> None:
        url = reverse("home")
        self.response = self.client.get(url)
    
    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)
        
    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, "home.html")
        
    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, "home page")
        
    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")
        
    def test_homepage_url_resolves_homepageview(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)
