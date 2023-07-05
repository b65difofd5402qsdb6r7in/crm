from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from .models import Client, Utilisateur
from .forms import ClientModelForm, UtilisateurModelForm, CustomUserCreationForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from django.contrib.auth.forms import UserCreationForm

class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    def get_success_url(self):
        return reverse("login")

class UtilisateurListView(ListView):
    template_name = "clients/utilisateurs.html"
    queryset = Utilisateur.objects.all()
    context_object_name = "utilisateurs"

class UtilisateurDetailView(DetailView):
    template_name = "clients/utilisateur_detail.html"
    queryset = Utilisateur.objects.all()
    context_object_name = "utilisateur"

class UtilisateurCreateView(CreateView):
    template_name = "clients/utilisateur_create.html"
    form_class = UtilisateurModelForm
    def get_success_url(self):
        return reverse("clients:utilisateur-list")

class UtilisateurUpdateView(UpdateView):
    template_name = "clients/utilisateur_update.html"
    queryset = Utilisateur.objects.all()
    form_class = UtilisateurModelForm
    def get_success_url(self):
        return reverse("clients:utilisateur-list")

class UtilisateurDeleteView(DeleteView):
    template_name = "clients/utilisateur_delete.html"
    queryset = Utilisateur.objects.all()
    def get_success_url(self):
        return reverse("clients:utilisateur-list")

class ClientListView(ListView):
    template_name = "clients/clients.html"
    queryset = Client.objects.all()
    context_object_name = "clients"

class ClientDetailView(DetailView):
    template_name = "clients/client_detail.html"
    queryset = Client.objects.all()
    context_object_name = "client"

class ClientCreateView(CreateView):
    template_name = "clients/client_create.html"
    form_class = ClientModelForm
    def get_success_url(self):
        return reverse("clients:list")

class ClientUpdateView(UpdateView):
    template_name = "clients/client_update.html"
    queryset = Client.objects.all()
    form_class = ClientModelForm
    def get_success_url(self):
        return reverse("clients:list")

class ClientDeleteView(DeleteView):
    template_name = "clients/client_delete.html"
    queryset = Client.objects.all()
    def get_success_url(self):
        return reverse("clients:list")



class PDFGeneratorView(View):
    def get(self, request, pk):
        try:
            client = Client.objects.get(id=pk)
        except Client.DoesNotExist:
            return HttpResponse("Client not found.", status=404)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="client_information.pdf"'

        # Create the PDF object
        doc = SimpleDocTemplate(response, pagesize=letter)
        elements = []

        # Define styles for the text
        styles = getSampleStyleSheet()
        header_style = styles['Heading1']
        normal_style = styles['Normal']
        bold_style = ParagraphStyle(name='Bold', parent=normal_style, fontName='Helvetica-Bold', spaceAfter=12)
        table_style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ])

        # Add content to the PDF
        elements.append(Paragraph("Client Information", header_style))
        elements.append(Spacer(1, 20))

        data = [
            [Paragraph("<b>Nom</b>", bold_style), client.nom],
            [Paragraph("<b>Prenom</b>", bold_style), client.prenom],
            [Paragraph("<b>Civilite</b>", bold_style), client.get_civilite_display()],
            [Paragraph("<b>Numero de Telephone</b>", bold_style), client.numero_telephone],
            [Paragraph("<b>Email</b>", bold_style), client.email],
            [Paragraph("<b>Siret</b>", bold_style), client.siret],
            [Paragraph("<b>Adresse</b>", bold_style), client.adresse],
            [Paragraph("<b>Ville</b>", bold_style), client.ville],
            [Paragraph("<b>Code Postal</b>", bold_style), client.code_postal],
            [Paragraph("<b>Nom de Societe</b>", bold_style), client.nom_societe],
            [Paragraph("<b>Statut Juridique</b>", bold_style), client.get_statut_juridique_display()],
            [Paragraph("<b>Commentaire</b>", bold_style), client.commentaire],
            [Paragraph("<b>Responsable Commercial</b>", bold_style), client.responsable_commercial.nom],
        ]

        table = Table(data, colWidths=[120, 300])
        table.setStyle(table_style)
        elements.append(table)

        # Build the PDF
        doc.build(elements)

        return response



# def reprint_signature_view(request, signature_id):
#     signature = get_object_or_404(Signature, id=signature_id)
#     return render(request, 'reprint_signature.html', {'signature': signature})

# def retrieve_signature_view(request):
#     signatures = Signature.objects.all()
#     return render(request, 'clients/retrieve_signature.html', {'signatures': signatures})

# def store_signature_view(request):
#     if request.method == 'POST':
#         signature_data = request.POST.get('signature_data')
#         signature = Signature(signature_data=signature_data)re
#         signature.save()
#         return redirect('clients/retrieve_signature')  
#     return render(request, 'clients/signature.html')

# def signature_view(request):
#     return render(request, 'clients/signature.html')