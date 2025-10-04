from django.core.files.storage import Storage
import cloudinary
import cloudinary.uploader
import sys


class CloudinaryStorage(Storage):
    """Storage backend customizado para Cloudinary"""
    
    def _save(self, name, content):
        """Upload do arquivo para Cloudinary"""
        print("=" * 60, file=sys.stderr)
        print("🔴 TENTANDO UPLOAD PARA CLOUDINARY", file=sys.stderr)
        print(f"Nome do arquivo: {name}", file=sys.stderr)
        print(f"Tipo do content: {type(content)}", file=sys.stderr)
        
        try:
            # Precisamos ler o conteúdo do arquivo
            if hasattr(content, 'read'):
                file_content = content.read()
                content.seek(0)  # Reset para caso precise ler novamente
            else:
                file_content = content
            
            print(f"Tamanho do arquivo: {len(file_content)} bytes", file=sys.stderr)
            
            # Upload para Cloudinary
            upload_result = cloudinary.uploader.upload(
                file_content,
                folder="media",
                resource_type="auto"
            )
            
            print(f"✅ UPLOAD SUCESSO!", file=sys.stderr)
            print(f"Public ID: {upload_result['public_id']}", file=sys.stderr)
            print(f"URL: {upload_result['secure_url']}", file=sys.stderr)
            print("=" * 60, file=sys.stderr)
            
            return upload_result['public_id']
            
        except Exception as e:
            print(f"❌ ERRO NO UPLOAD: {e}", file=sys.stderr)
            print(f"Tipo do erro: {type(e)}", file=sys.stderr)
            import traceback
            traceback.print_exc(file=sys.stderr)
            print("=" * 60, file=sys.stderr)
            raise
    
    def url(self, name):
        """Retorna a URL do arquivo no Cloudinary"""
        if not name:
            return ''
        try:
            url = cloudinary.CloudinaryImage(name).build_url()
            print(f"📸 URL gerada: {url}", file=sys.stderr)
            return url
        except Exception as e:
            print(f"❌ Erro ao gerar URL: {e}", file=sys.stderr)
            return ''
    
    def exists(self, name):
        """Verifica se arquivo existe"""
        return False
    
    def delete(self, name):
        """Deleta arquivo do Cloudinary"""
        try:
            cloudinary.uploader.destroy(name)
            print(f"🗑️ Arquivo deletado: {name}", file=sys.stderr)
        except Exception as e:
            print(f"❌ Erro ao deletar: {e}", file=sys.stderr)
    
    def size(self, name):
        """Retorna tamanho do arquivo"""
        return 