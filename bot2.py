""""
bot

Tutorial program for PRAW:
See https://github.com/praw-dev/praw/wiki/Writing-A-Bot/

Autor: Negaly
"""
#Importamos funciones basicas de bot y de temporizacion
import time
import praw
import pprint
user = " "
psswrd = " "
subreddit = " "
'''
Iniciacion de variables
'''
def init():
    infile = open('config.txt', 'r') # Indicamos el valor 'w'.
    arraylineas = infile.readlines()    
    user = str(arraylineas[0].split(" ")[1])
    psswrd = str(arraylineas[1].split(" ")[1])
    subreddit = str(arraylineas[2].split(" ")[1])
    r.login(username = user.rstrip(),password = psswrd.rstrip())

    infile.close()
    return subreddit 
'''
def buscaPropuestas(limite):
    @limite permite seleccionar cuantos hilos busca en cada vuelta
 unicode a UTF-8 -> .encode("UTF-8")
    buscaPropuestas recorre los ultimos hilos, buscando cuales pertenecen a la categoria propuestas.
'''
def buscaPropuestas(limite):
    msg= ""
    infile = open('already_done.txt', 'r+') # Indicamos el valor 'w'.
    already_done = infile.readlines()
    print(already_done)
    cont=1
    numero= len(already_done)
    for submission in subreddit.get_new(limit=limite):        
        # Test if it contains a new post
        if submission.id+'\n' not in already_done and (submission.link_flair_css_class=='propuesta'):
          #HIPERVINCULOS msg += '['+submission.title+'](%s)' % submission.short_link
            msg += str(len(already_done)+cont) 
            msg += '  '
            msg += submission.short_link
            msg += ' %s ' % submission.title
            msg += '\n'
            cont += 1
            infile.write(submission.id+'\n')
    infile.close()
    outfile = open('listadelinks.txt', 'a') # Indicamos el valor 'w'.
    outfile.write(msg.encode("UTF-8"))
    outfile.close()        
    #submission = r.get_submission(submission_id = "2ge35o")
    #print(submission.link_flair_css_class)
    #print(submission.link_flair_text)
    #r.send_message('Negaly', 'Titles', msg)
    return already_done
'''Main'''
def datosExcel():
    for submission_id in already_done:
        submission = r.get_submission(submission_id = submission_id.strip())
         #AUTOR/A DE LA PROPUESTA QUIEN HA ESCRITO LA SINTESIS    PUNTUACION  COMENTARIOS PORCENTAJE votos positivos  FECHA CREACION  FECHA SINTESIS  RESPONSABLE DE 2a REVISION  ESTADO DE 2a REVISION   LINK A SINTESIS
        excelMsg=""
        outfile = open('almacenPropuestas.txt', 'a') # Indicamos el valor 'w'.
        excelMsg += "NUMERO DE LA PROPUESTA LINK HILO;"
        excelMsg += submission.title+";" #NOMBRE DE LA PROPUESTA
        excelMsg += ";;;;" # 4 vacios -> 1er/a REVISOR/A - RESPONSABLE   ESTADO DE LA SINTESIS CATEGORIA
        excelMsg += str(submission.author) + ';' #AUTOR/A DE LA PROPUESTA
        #print(excelMsg)
        outfile.write(excelMsg.encode("UTF-8"))
        outfile.close()     
#No se para que se hace esto, pero supongo que es para decirle a reddit que bot somos (no lo he cambiado pero lo hare en un futuro)
r = praw.Reddit('PRAW related-question monitor by u/_Daimon_ v 1.0.'
                'Url: https://praw.readthedocs.org/en/latest/'
                'pages/writing_a_bot.html')
subreddit = init()
print "Inicio"
while True:
    print ('vuelta')
    subreddit = r.get_subreddit(subreddit)
    already_done = buscaPropuestas(10)
    datosExcel()
    break #Para ir haciendo pruebas
    time.sleep(1800)  
