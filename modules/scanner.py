import requests
from abc import ABC, abstractmethod

# Modul 6: Abstraction (Abstract Base Class)
class VulnerabilityScanner(ABC):
    def __init__(self, target_url):
        # Modul 6: Encapsulation (Private Variable)
        self.__target_url = target_url

    # Modul 6: Getter
    def get_url(self):
        return self.__target_url

    # Modul 6: Setter
    def set_url(self, new_url):
        self.__target_url = new_url

    # Abstract method yang wajib di-override (Polymorphism)
    @abstractmethod
    def scan(self):
        pass

# Modul 5: Class & Object (Inheritance)
class LFIScanner(VulnerabilityScanner):
    def __init__(self, target_url, payloads):
        super().__init__(target_url)
        # Modul 1: Array/List (Menyimpan payloads)
        self.payloads = payloads 

    # Modul 6: Polymorphism (Implementasi method scan)
    def scan(self, log_queue):
        results = []
        print(f"Memulai scan pada: {self.get_url()}")
        
        # Modul 2: Perulangan (Iterasi payload)
        for payload in self.payloads:
            full_url = f"{self.get_url()}{payload}"
            try:
                # Request sederhana
                response = requests.get(full_url, timeout=2)
                
                # Modul 3: Pengkondisian (Cek status code)
                if response.status_code == 200:
                    msg = f"[VULN] Ditemukan: {full_url}"
                    results.append(msg)
                else:
                    msg = f"[SAFE] Aman ({response.status_code}): {payload}"
                
                # Masukkan ke Queue (Modul 7)
                log_queue.enqueue(msg)
                
            except Exception as e:
                log_queue.enqueue(f"[ERROR] {str(e)}")
        
        return results