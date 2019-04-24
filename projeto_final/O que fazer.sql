Parsing de arquivos
Criação de APIs
Django Web
Persistência de dados
Análise de dados

Ideias
Brasil IO;
Balneabilidade FATMA (https://github.com/daniboy000/sc_aguas);
Portal da Transparência (http://www.portaltransparencia.gov.br/download-de-dados/orcamhttps://data.unicef.org/resources/resource-type/datasets/ento-despesa);
Histórico de valores da Bolsa (Café, Açúcar, Ouro etc);
Levantamento de dados dos estados da federação.
Unicef (https://data.unicef.org/resources/resource-type/datasets/)
API FATMA
https://balneabilidade.ima.sc.gov.br/municipio/getMunicipios

response:
[{"CODIGO":"10","DESCRICAO":"ARARANGUA"},{"CODIGO":"12","DESCRICAO":"BALN. ARROIO DO SILVA"},{"CODIGO":"14","DESCRICAO":"BALN. GAIVOTA"},{"CODIGO":"24","DESCRICAO":"BALNE\u00c1RIO CAMBORI\u00da"},{"CODIGO":"18","DESCRICAO":"BALNE\u00c1RIO DA BARRA DO SUL"},{"CODIGO":"9","DESCRICAO":"BALNEARIO RINC\u00c3O"},{"CODIGO":"19","DESCRICAO":"BARRA VELHA"},{"CODIGO":"1","DESCRICAO":"BIGUA\u00c7\u00da"},{"CODIGO":"27","DESCRICAO":"BOMBINHAS"},{"CODIGO":"2","DESCRICAO":"FLORIAN\u00d3POLIS"},{"CODIGO":"5","DESCRICAO":"GAROPABA"},{"CODIGO":"28","DESCRICAO":"GOVERNADOR CELSO RAMOS"},{"CODIGO":"6","DESCRICAO":"IMBITUBA"},{"CODIGO":"23","DESCRICAO":"ITAJA\u00cd"},{"CODIGO":"25","DESCRICAO":"ITAPEMA"},{"CODIGO":"15","DESCRICAO":"ITAPO\u00c1"},{"CODIGO":"8","DESCRICAO":"JAGUARUNA"},{"CODIGO":"16","DESCRICAO":"JOINVILLE"},{"CODIGO":"7","DESCRICAO":"LAGUNA"},{"CODIGO":"22","DESCRICAO":"NAVEGANTES"},{"CODIGO":"4","DESCRICAO":"PALHO\u00c7A"},{"CODIGO":"11","DESCRICAO":"PASSO DE TORRES"},{"CODIGO":"29","DESCRICAO":"PAULO LOPES"},{"CODIGO":"21","DESCRICAO":"PENHA"},{"CODIGO":"20","DESCRICAO":"PI\u00c7ARRAS"},{"CODIGO":"26","DESCRICAO":"PORTO BELO"},{"CODIGO":"13","DESCRICAO":"PRAIA DO ARROIO DO SILVA (Ponto 01)"},{"CODIGO":"17","DESCRICAO":"S\u00c3O FRANCISCO DO SUL"},{"CODIGO":"3","DESCRICAO":"S\u00c3O JOS\u00c9"}]
https://balneabilidade.ima.sc.gov.br/local/getLocaisByMunicipio

body
data = {
	municipioID: 10
}
https://balneabilidade.ima.sc.gov.br/pontoColeta/getPontosByLocal

body
data = {
	localID: 74
}
response:
[{"CODIGO":"254","NOME":"Ponto 33","OCULTAR":"N","LOCAL_ID":"74","LOCALIZACAO":"EM FRENTE AO POSTO SALVA VIDAS","LATITUDE":"-27.62907846483125","LONGITUDE":"-48.44823099512896","CONDICAO":"PR\u00d3PRIO"}]
© 2019 GitHub, Inc.