import os
from django.shortcuts import render
from django.http import FileResponse
from .forms import UploadArquivoForm
from .conversor_pptx_para_latex import converter_pptx_para_latex

def upload_arquivo(request):
    if request.method == "POST":
        form = UploadArquivoForm(request.POST, request.FILES)
        if form.is_valid():
            arquivo = request.FILES["arquivo"]
            caminho_arquivo = f"./temp_{arquivo.name}"
            
            with open(caminho_arquivo, "wb+") as destino:
                for chunk in arquivo.chunks():
                    destino.write(chunk)

            zip_gerado = converter_pptx_para_latex(caminho_arquivo)

            os.remove(caminho_arquivo)

            response = FileResponse(open(zip_gerado, 'rb'), as_attachment=True, filename=os.path.basename(zip_gerado))
            return response
    else:
        form = UploadArquivoForm()

    return render(request, "conversor/upload.html", {"form": form})
