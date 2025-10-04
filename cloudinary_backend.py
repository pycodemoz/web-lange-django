from django.core.files.storage import Storage
from django.core.files.base import ContentFile
import cloudinary
import cloudinary.uploader
from urllib.parse import urljoin


class CloudinaryStorage(Storage):
    """Storage backend customizado para Cloudinary"""
    
    def _save(self, name, content):
        """Upload do arquivo para Cloudinary"""
        try:
            # Upload para Cloudinary
            upload_result = cloudinary.uploader.upload(
                content,
                folder="media",  # pasta no Cloudinary
                resource_type="auto"
            )
            # Retorna o public_id
            return upload_result['public_id']
        except Exception as e:
            print(f"Erro ao fazer upload para Cloudinary: {e}")
            raise
    
    def url(self, name):
        """Retorna a URL do arquivo no Cloudinary"""
        if not name:
            return ''
        try:
            # Gera URL do Cloudinary
            return cloudinary.CloudinaryImage(name).build_url()
        except Exception as e:
            print(f"Erro ao gerar URL: {e}")
            return ''
    
    def exists(self, name):
        """Verifica se arquivo existe (sempre retorna False para forçar novo upload)"""
        return False
    
    def delete(self, name):
        """Deleta arquivo do Cloudinary"""
        try:
            cloudinary.uploader.destroy(name)
        except Exception as e:
            print(f"Erro ao deletar: {e}")
    
    def size(self, name):
        """Retorna tamanho do arquivo"""
        return 0