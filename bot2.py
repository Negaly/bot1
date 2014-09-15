""""
bot podemos

Tutorial program for PRAW:
See https://github.com/praw-dev/praw/wiki/Writing-A-Bot/

Autor: Negaly
"""
#Importamos funciones basicas de bot y de temporizacion
import time
import praw
import pprint
'''
def buscaPropuestas(limite):
    @limite permite seleccionar cuantos hilos busca en cada vuelta

    buscaPropuestas recorre los ultimos hilos, buscando cuales pertenecen a la categoria propuestas.
'''
def buscaPropuestas(limite):
    msg= ""
    for submission in subreddit.get_new(limit=limite):
        # Test if it contains a new post
        if submission.id not in already_done and (submission.link_flair_css_class=='propuesta'):
          #HIPERVINCULOS msg += '['+submission.title+'](%s)' % submission.short_link
            msg += '%s \n' % submission.title
            already_done.append(submission.id)
    outfile = open('texto.txt', 'a') # Indicamos el valor 'w'.
    outfile.write(msg.encode("UTF-8"))
    outfile.close()        
    #submission = r.get_submission(submission_id = "2ge35o")
    #print(submission.link_flair_css_class)
    #print(submission.link_flair_text)
    #r.send_message('Negaly', 'Titles', msg)
    return msg

'''Main'''
#No se para que se hace esto, pero supongo que es para decirle a reddit que bot somos (no lo he cambiado pero lo hare en un futuro)
r = praw.Reddit('PRAW related-question monitor by u/_Daimon_ v 1.0.'
                'Url: https://praw.readthedocs.org/en/latest/'
                'pages/writing_a_bot.html')
r.login()
print "Inicio"
while True:
    already_done = []
    print ('vuelta')
    subreddit = r.get_subreddit('podemos')
    buscaPropuestas(10)
    time.sleep(1800)  
