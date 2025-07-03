class WebsiteNotSupportedError(Exception):
    def __init__(self, domain: str):
        self.domain = domain
        super().__init__(f"Website '{domain}' is not supported yet.")
