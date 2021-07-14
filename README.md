# mattos.proxie

Foi desenvolvido com objetivo de prover lista de proxies grátis para utilização. A lista de proxie fornecida é baseada na lista free disponibilizada pela SLL Proxie List, e basicamente o que fazemos é disponibizar um formato JSON mais amigavel para se trabalhar com suas aplicações, para isso utilizamos Python, Flask e Beautifulsoup4. O código fonte pode ser obtido no GitHub do desenvolvedor Michael de Mattos O software hoje é fornecido sobre a licença GNU Lesser General Public License 100% Livre de Royalty. 

# Instalação 
-- Python3.7 ou superior
<code>pip3 install -r requeriments.pip3</code>

# Documentação da API
Para visualizar a documentação execute o script wsgi.py e acesse a aplicação no endereço http://127.0.0.1:5000/

# Consumindo a API via Python com requests
<code>
import requests
  
r = requests.get("http://127.0.0.1:5000/br")

r.json()

[
 {
    "anonymity": "elite proxy", 
    "country": "Brazil", 
    "google": "no", 
    "hostname": "191.7.210.162", 
    "https": "yes", 
    "id_country": "BR", 
    "last_checked": "1 minute ago", 
    "port": "35820"
  }, 
]
</code>
