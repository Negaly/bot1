""""
bot podemos

Tutorial program for PRAW:
See https://github.com/praw-dev/praw/wiki/Writing-A-Bot/

Autor: Negaly
"""
#Importamos funciones basicas de bot y de temporizacion
import time
import praw

#No se para que se hace esto, pero supongo que es para decirle a reddit que bot somos (no lo he cambiado pero lo hare en un futuro)
r = praw.Reddit('PRAW related-question monitor by u/_Daimon_ v 1.0.'
                'Url: https://praw.readthedocs.org/en/latest/'
                'pages/writing_a_bot.html')

r.login()
already_done = []

prawWords = ['praw', 'reddit_api', 'mellort']
msg= ""
while True:
    subreddit = r.get_subreddit('podemos')
    for submission in subreddit.get_new(limit=10):
        print "vuelta"
        # Test if it contains a new post
        if submission.id not in already_done:
          #HIPERVINCULOS msg += '['+submission.title+'](%s)' % submission.short_link
            msg += '%s \n' % submission.title

            already_done.append(submission.id)
    outfile = open('texto.txt', 'a') # Indicamos el valor 'w'.
     
    print (msg)

    outfile.write(msg.encode("UTF-8"))
    outfile.close()        


    #r.send_message('Negaly', 'Titles', msg)
    break    
#time.sleep(1800)