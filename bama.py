'''
website ha az tarighe header e `user-agent` hasteshke mifahman shoma robot hastin ya na
masaaln tooye website www.bama.ir vaghti hamintori ba mororgar miri dakhelesh,  hamechi
ok e vali vaghti ba code ba package request bekhat beri dakhelesh behet error 403 mide 
mifahme robot i va adam nisti vaseye inke doresh bezanim va nafahme ke robot hastim,
mitonim behesh headers ezafe konim. bayad tooye mororgar aval bama ro baz konim bad 
inspect ro beanim berim too bakhshe network badesh header ha ro negah konim donballe
key `user-agent` migardim va meghdare value esh ro peyda mikonim copy mikonim hala 
toye codemon age code e zir ro bezanim mizare darkhast befrestim va ok mide
'''
 
import requests 

url= 'https://bama.ir/'
response= requests.get(url, headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'})
print(response.reason)