# remember!

Um sistema legal que, ao solicitar o nick de um player de osu! (ohio state university), seleciona alguns mapas que ele já jogou e os exibe.<br><br>

## importante:


é preciso baixar essas coisas:
```
pip install ossapi
pip install aiohttp
```
alternativamente, use [esse ](https://pypi.org/project/ossapi/#files) e [esse link](https://pypi.org/project/aiohttp/#files) para baixar os bglh (respectivo ao trecho acima).
<h2></h2>


Além do mais, c tbm precisa ir no site do osu e criar uma nova porrinha dessas dai:

![image](https://github.com/user-attachments/assets/107e8d04-ba24-42d7-9d51-c36b83019db1)

e colocar no programa:

```python
api = OssapiAsync(0, "suassenha:)") #idcliente e senha. pra cirar vai no site do osu configuracoes da conta (leia docs)
```

<h2></h2>

#### Não fica spammando a API, é contra os [[termos de uso]](https://osu.ppy.sh/docs/#terms-of-use) ; [[mais info ossapi]](https://github.com/tybug/ossapi)
