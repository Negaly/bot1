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
import datetime 
import shutil
user = " "
psswrd = " "
subreddit = " "
'''
        Iniciacion de variables
        init(fichero)
        carga los valores iniciales de usuario contrasea y subreddit, de un fichero externo que se le pasa como parametro'''
def init(fichero):
    infile = open(str(fichero), 'r') # Indicamos el valor 'w'.
    arraylineas = infile.readlines()    
    user = str(arraylineas[0].split(" ")[1])
    psswrd = str(arraylineas[1].split(" ")[1])
    subreddit = str(arraylineas[2].split(" ")[1])
    r.login(username = user.rstrip(),password = psswrd.rstrip())
    infile.close()
    return subreddit 
'''def buscaPropuestas(limite):
    @limite permite seleccionar cuantos hilos busca en cada vuelta
 unicode a UTF-8 -> .encode("UTF-8")
    buscaPropuestas recorre los ultimos hilos, buscando cuales pertenecen a la categoria propuestas.'''
def buscaPropuestas(limite):
    msg= ""
    already_done = readFile('already_done.txt')
    cont=1
    numero= len(already_done)
    for submission in subreddit.get_new(limit=limite):        
        # Comprobamos si es una propuesta
        if submission.id+'\n' not in already_done and (submission.link_flair_css_class=='propuesta'):
            msg += str(len(already_done)+cont) 
            msg += '  '
            msg += submission.short_link
            msg += ' %s ' % submission.title
            msg += '\n'
            cont += 1
            text = submission.id+'\n'
            writeFile(text,'already_done.txt')
    writeFile(msg,'listadelinks.txt')   
    return already_done
''' writeFile(text,dirFile)
    outfile = open('listadelinks.txt', 'a') # Indicamos el valor 'w'.
    outfile.write(msg.encode("UTF-8"))
    outfile.close()'''
def writeFile(text,dirFile):
    outfile = open(str(dirFile), 'a') # Indicamos el valor 'w'.
    outfile.write(text.encode("UTF-8"))
    outfile.close()
'''
 writeFile(text,dirFile)
    outfile = open('listadelinks.txt', 'a') # Indicamos el valor 'w'.
    outfile.write(msg.encode("UTF-8"))
    outfile.close()'''
def readFile(dirFile):
    infile = open(str(dirFile), 'r+') # Indicamos el valor 'w'.
    already_done = infile.readlines()
    infile.close()
    return already_done
'''
 vueltaTxt(inFile,outFile): 
    infile, fichero con una lista
    outfile, fichero generado con la misma lista dada la vueltaTxt'''
def vueltaTxt(inFile,outFile):

    infile = open(str(inFile, 'r')) # Indicamos el valor 'w'.
    arraylineas = inFile.readlines() 
    infile.close()

    outfile = open('volteado.txt', 'a') # Indicamos el valor 'w'.
    for line in range (1,len(arraylineas)+1):
        outfile.write(arraylineas[-line])
    outfile.close()
def copyFile(src, dest):
    try:
        shutil.copy(src, dest)
    # eg. src and dest are the same file
    except shutil.Error as e:
        print('Error: %s' % e)
    # eg. source or destination doesn't exist
    except IOError as e:
        print('Error: %s' % e.strerror)


'''Main'''
def datosExcel():
    for submission_id in already_done:
        submission = r.get_submission(submission_id = submission_id.strip())
         # PORCENTAJE votos positivos  FECHA CREACION  FECHA SINTESIS  RESPONSABLE DE 2a REVISION  ESTADO DE 2a REVISION   LINK A SINTESIS
        excelMsg=""
        excelMsg += "NUMERO;"
        excelMsg += submission.short_link+';'
        excelMsg += submission.title+";" #NOMBRE DE LA PROPUESTA
        excelMsg += ";;;" # 4 vacios -> 1er/a REVISOR/A - RESPONSABLE   ESTADO DE LA SINTESIS CATEGORIA
        excelMsg += str(submission.author) + ';' #AUTOR/A DE LA PROPUESTA
        excelMsg += ';'+ str(submission.score) + ';' + str(submission.num_comments) + ';' #QUIEN HA ESCRITO LA SINTESIS PUNTUACION  COMENTARIOS
        #Porcentaje 
        if (submission.downs == 0): 
            excelMsg += '1;'
        else: 
            excelMsg += str(submission.ups/submission.downs)+';'
        excelMsg += str(submission.created_utc)+';'
        excelMsg += '\n'
        #print(excelMsg)
        writeFile(excelMsg,'almacenPropuestas.txt')   
#No se para que se hace esto, pero supongo que es para decirle a reddit que bot somos (no lo he cambiado pero lo hare en un futuro)
r = praw.Reddit('PRAW related-question monitor by u/_Daimon_ v 1.0.'
                'Url: https://praw.readthedocs.org/en/latest/'
                'pages/writing_a_bot.html')
subreddit2 = init('config.txt')
print "Inicio"
while True:
    print ('vuelta en la fecha: ' + str(datetime.datetime.now()))
    subreddit = r.get_subreddit(subreddit2)
    buscaPropuestas(10)
#Aqui lo del excel
    #already_done = readFile('already_done.txt')
    #datosExcel()
    #copyFile('listadelinks.txt','/home/ignacio/Dropbox/DocsBot/listadelinks.txt')
    #copyFile('almacenPropuestas.txt','/home/ignacio/Dropbox/DocsBot/almacenPropuestas.txt')
    break #Para ir haciendo pruebas
    time.sleep(1800)  

'''
    submission = r.get_submission(submission_id = "2ge35o")
    print(submission.link_flair_css_class)
    print(submission.link_flair_text)
    r.send_message('Negaly', 'Titles', msg)
    HIPERVINCULOS msg += '['+submission.title+'](%s)' % submission.short_link
'''