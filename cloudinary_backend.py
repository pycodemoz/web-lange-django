from django.core.files.storage import Storage
import cloudinary
import cloudinary.uploader


class CloudinaryStorage(Storage):
    """Storage backend customizado para Cloudinary"""
    
    def _save(self, name, content):
        """Upload do arquivo para Cloudinary"""
        if hasattr(content, 'read'):
            file_content = content.read()
            content.seek(0)
        else:
            file_content = content
        
        upload_result = cloudinary.uploader.upload(
            file_content,
            folder="media",
            resource_type="auto"
        )
        
        return upload_result['public_id']
    
    def url(self, name):
        """Retorna a URL do arquivo no Cloudinary"""
        if not name:
            return ''
        return cloudinary.CloudinaryImage(name).build_url()
    
    def exists(self, name):
        return False
    
    def delete(self, name):
        try:
            cloudinary.uploader.destroy(name)
        except:
            pass
    
    def size(self, name):
        return 0