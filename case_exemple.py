class AlgumaCoisa:
    def diga_ola(self):
        print('olá Mundo!!!!')
        
    def __enter__(self):
        print('Entrando no contexto')
        return self 
    def __exit__(self,exc_type,exc_val,exc_tb):
        print('Saindo do contexto')
        
with AlgumaCoisa() as ola:
    ola.diga_ola()
    print('Estou no meio')