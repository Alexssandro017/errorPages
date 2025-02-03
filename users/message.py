class message:
    def __init__(self, type: str, message: str, code: int, img: str = None):
        self.type = type  # Tipo de mensaje (ejemplo: "error", "info", "success")
        self.message = message  # Contenido del mensaje
        self.code = code  # Código de estado (ejemplo: 200, 400, 500)
        self.img = img  # Imagen opcional para el mensaje

    def __str__(self):
        return f"[{self.type.upper()}] Código {self.code}: {self.message} (Imagen: {self.img})"

    def to_dict(self):
        return {
            "tipo": self.type,
            "mensaje": self.message,
            "codigo": self.code,
            "imagen": self.img
        }
