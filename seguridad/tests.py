from django.test import TestCase, SimpleTestCase

from django.urls import reverse, resolve

from .forms import SeguridadForm, AfectadosFormSet
from .views import SeguridadCreate

class AboutPageTest(SimpleTestCase):

    def setUp(self):
        self.response = self.client.get(reverse("seguridad:about"))
    
    def test_url_about(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_hrml_about(self):
        self.assertTemplateUsed(self.response, "seguridad/seguridad_about.html")
        self.assertContains(self.response, "Acerca de...")
        self.assertNotContains(self.response, "About...")
        
class RegistroCasosTest(TestCase):
    def setUp(self):
        url = reverse("seguridad:seguridad_new")
        self.response = self.client.get(url)
        
        
    def test_casos_registro(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "seguridad/seguridad_form.html")
        self.assertContains(self.response, "Evento de seguridad")
    
    def test_registro_form(self):
        print(self.response)
        form = self.response.ctx.get("named_formsets")
        self.assertIsInstance(form, SeguridadForm)
        self.assertContains(self.response, "csrfmiddlewaretoken")
    
    def test_registro_casos_vista(self):
        view = resolve("/seguridad/add/seguridad")
        self.assertEqual(view.func.__name__, SeguridadCreate.as_view().__name__)
          
            
            
    
    
        
    
    