class teleCommands(object):
    def __init__(self, kord, connection):
        self.kord = kord
        self.connection = connection
    
    
    #HELP
    def send_help(self, message):
        print(message)
        self.kord.send_message(message.chat.id, 'Hola!')
        self.kord.send_message(message.chat.id, 'Soy el Entrenador Kord y estoy aquí para ayudarte! Puedes pedirme informacion de pokemon salvajes y de jefes de raids con los comandos select y select_boss')
        self.kord.send_message(message.chat.id, 'Aunque aún no sea un profesor pokemon, tengo muchos datos para tí, no dudes en preguntar!')
        self.kord.send_message(message.chat.id, 'Cuando esté listo para el publico pondré el enlace a la documentacion de github, pero ahora mismo me da pereza')
        self.kord.delete_message(message.chat.id, message.message_id)
    #KILL
    def kill_message(self, message):
        print(message)
        if(message.from_user.username == "ALK222"): #Gracias Willson por ayudarnos a hacer que los comandos se pudiesen asignar a usuarios
            self.kord.send_message(message.chat.id, "Hello, master ")
            self.kord.delete_message(message.chat.id, message.message_id)
    

    # #INSERT(ONLY DEBUG)
    # def insert_into(self, message):
    #     split = message.text.split()
    #     if (len(split) != 5):
    #         kord.reply_to(message, "numero de argumentos erroneo, pruebe de nuevo")
    #     else:
    #         try:
    #             with connection.cursor() as cursor:
    #             #buscamos el pokemon en la tabla
    #                 sql = "SELECT nombre FROM pokemon where nombre like '" + split[2].upper() + "'"
    #                 cursor.execute(sql)
    #                 cursor.fetchall()
    #                 #si el resultado de la consulta es vacio, quiere decir que no
    #                 #existe y por tanto se puede añadir
    #                 if(cursor.rowcount != 0):
    #                     kord.send_message(message.chat.id, "El pokemon ya está registrado en la pokedex")
    #                 else:
    #                     sql = "INSERT INTO `pokemon` (`numdex`, `nombre`, `kmpercandy`, `category`) VALUES (%s, %s, %s, %s)"
    #                     cursor.execute(sql, (split[1], split[2].upper(), split[3], split[4].upper()))
    #                     kord.send_message(message.chat.id, "pokemon añadido satisfactoriamente")
                    

    #             # connection is not autocommit by default.  So you must commit to
    #             # save
    #             # your changes.
    #             connection.commit()
    #         finally:
    #             kord.delete_message(message.chat.id, message.message_id)

    # #INSERT_POKEMON(ONLY DEBUG)
    # def insert_pokemon(self, message):
    #     split = message.text.split()
    #     print(split)
    #     if (len(split) != 3):
    #         kord.reply_to(message, "numero de argumentos erroneo, pruebe de nuevo")
    #     else:
    #         try:
    #             with connection.cursor() as cursor:
    #                 print(split[1].upper())
    #             # Create a new record
    #                 sql = "SELECT `nombre_w` FROM `wild` where 'nombre_w' like '" + split[1].upper() + "'"
    #                 cursor.execute(sql)
    #                 print(cursor.fetchall())
    #                 if(cursor.rowcount != 0):
    #                     self.kord.send_message(message.chat.id, "ese pokemon ya esta en la tabla")
    #                 else:
    #                     sql = "SELECT nombre FROM pokemon where nombre like '" + split[1].upper() + "'"
    #                     cursor.execute(sql)
    #                     cursor.fetchall()
    #                 #si el resultado de la consulta es vacio, quiere decir que no
    #                 #existe y por tanto se puede añadir
    #                     if(cursor.rowcount != 0):
    #                         sql = "INSERT INTO wild (nombre_w, pc100) VALUES (%s, %s)"
    #                         cursor.execute(sql, (split[1].upper(), split[2]))
    #                         self.kord.send_message(message.chat.id, "pokemon añadido satisfactoriamente")
    #                     else:
    #                         self.kord.send_message(message.chat.id, "Inserte primero el pokemon en la tabla Pokemon")
                    

    #             # connection is not autocommit by default.  So you must commit to
    #             # save
    #             # your changes.
    #             connection.commit()
    #         finally:
    #             kord.delete_message(message.chat.id, message.message_id)


    # #INSERT_BOSS(ONLY DEBUG)
    # @kord.message_handler(commands=['insert_boss'])
    # def insert_boss(self, message):
    #     split = message.text.split()
    #     print(split)
    #     if (len(split) != 4):
    #         kord.reply_to(message, "numero de argumentos erroneo, pruebe de nuevo")
    #     else:
    #         try:
    #             with connection.cursor() as cursor:
    #             # Create a new record
    #                 sql = "SELECT `nombre_b` FROM `boss` where 'nombre_b' like '" + split[1].upper() + "'"
    #                 cursor.execute(sql)
    #                 cursor.fetchall()
    #                 if(cursor.rowcount != 0):
    #                     kord.send_message(message.chat.id, "ese pokemon ya esta en la tabla")
    #                 else:
    #                     sql = "SELECT nombre FROM pokemon where nombre like '" + split[1].upper() + "'"
    #                     cursor.execute(sql)
    #                     cursor.fetchall()
    #                 #si el resultado de la consulta es vacio, quiere decir que no
    #                 #existe y por tanto se puede añadir
    #                     if(cursor.rowcount != 0):
    #                         sql = "INSERT INTO boss (nombre_b, pc100, pc100boost) VALUES (%s, %s, %s)"
    #                         cursor.execute(sql, (split[1].upper(), split[2], split[3]))
    #                         kord.send_message(message.chat.id, "pokemon añadido satisfactoriamente")
    #                     else:
    #                         kord.send_message(message.chat.id, "Inserte primero el pokemon en la tabla Pokemon")
    #                         kord.send_message(message.chat.id, "pokemon añadido satisfactoriamente")
                    

    #             # connection is not autocommit by default.  So you must commit to
    #             # save
    #             # your changes.
    #             connection.commit()
    #         finally:
    #             kord.delete_message(message.chat.id, message.message_id)


    #SELECT
    def select(self, message):
        split = message.text.split()
        if(len(split) > 1):
            with self.connection as cursor:
                sql = "SELECT pokemon.NUMDEX, pokemon.NOMBRE, pokemon.KMPERCANDY, wild.pc100 FROM pokemon JOIN wild WHERE pokemon.nombre LIKE '" + split[1] + "' AND wild.NOMBRE_W LIKE '" + split[1] + "'"
                cursor.execute(sql)
                if(cursor.rowcount != 0):
                    result = str(cursor.fetchall())
                    mensaje = result.split()
                    if(int(mensaje[1].replace(',', '')) < 10):
                        prueba = '0' + mensaje[1]
                        mensaje[1] = prueba
                    if(int(mensaje[1].replace(',', '')) < 100):
                        prueba = '0' + mensaje[1]
                        mensaje[1] = prueba
                    self.kord.send_photo(message.chat.id, 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/' + mensaje[1].replace(',', '') + '.png')
                    self.kord.send_message(message.chat.id, self.info_pokemon(result))
                else:
                    self.kord.send_message(message.chat.id, "El pokemon no está en la pokedex")
        else:
            self.kord.send_message(message.chat.id, 'Introduzca un argumento valido')
        self.kord.delete_message(message.chat.id, message.message_id)        

            
    # #DEBUG ONLY
    # @kord.message_handler(commands=['ini'])
    # def ini(message):
    #     f = open("wild.txt", "r")
    #     while(True):
    #         linea = f.readline()
    #         if not linea:
    #             break
    #         split = linea.split()
    #         with connection.cursor() as cursor:
    #             # Create a new record
    #             sql = "SELECT `nombre_w` FROM `wild` where 'nombre_w' like '" + split[0].upper() + "'"
    #             cursor.execute(sql)
    #             print(cursor.fetchall())
    #             if(cursor.rowcount != 0):
    #                 print('f')
    #             else:
    #                 sql = "SELECT nombre FROM pokemon where nombre like '" + split[0].upper() + "'"
    #                 cursor.execute(sql)
    #                 cursor.fetchall()
    #             #si el resultado de la consulta es vacio, quiere decir que no
    #             #existe y por tanto se puede añadir
    #                 if(cursor.rowcount != 0):
    #                     print(split[0].upper())
    #                     sql = "INSERT INTO WILD (NOMBRE_W, PC100) VALUES (%s, %s)"
    #                     cursor.execute(sql, (split[0].upper(), split[1]))
    #                 else:
    #                     print('f')
    #             connection.commit()
                
        
    #     f.close()

    #INFOPOKEMON
    def info_pokemon(self, result):
        mensaje = result.replace('[', '')
        mensaje = mensaje.replace(']', '')
        mensaje = mensaje.replace('{', '')
        mensaje = mensaje.replace('}', '')
        mensaje = mensaje.replace(',', '')
        mensaje = mensaje.replace(':', '')
        mensaje = mensaje.replace("'", '')
        mensaje = mensaje.split()
        final = "Nº: " + mensaje[1] + "\n"
        final += "Nombre: " + mensaje[3] + "\n"
        final += "Km para caramelo: " + mensaje[5] + "\n"
        final += "PC 100: " + mensaje[7] + "\n"
        return final



    #SELECT BOSS
    def select_boss(self, message):
        split = message.text.split()
        if(len(split) > 1):
            with self.connection as cursor:
                sql = "SELECT pokemon.NUMDEX, pokemon.NOMBRE, pokemon.KMPERCANDY, boss.pc100, boss.pc100boost FROM pokemon JOIN boss WHERE pokemon.nombre LIKE '" + split[1] + "' AND boss.nombre_b LIKE '" + split[1] + "'"
                cursor.execute(sql)
                if(cursor.rowcount != 0):
                    result = str(cursor.fetchall())
                    mensaje = result.split()
                    if(int(mensaje[1].replace(',', '')) < 10):
                        prueba = '0' + mensaje[1]
                        mensaje[1] = prueba
                    if(int(mensaje[1].replace(',', '')) < 100):
                        prueba = '0' + mensaje[1]
                        mensaje[1] = prueba
                    self.kord.send_photo(message.chat.id, 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/' + mensaje[1].replace(',', '') + '.png')
                    self.kord.send_message(message.chat.id, self.info_boss(result))
                else:
                    self.kord.send_message(message.chat.id, "El pokemon no está en la pokedex")
        else:
            self.kord.send_message(message.chat.id, 'Introduzca un argumento valido')
        self.kord.delete_message(message.chat.id, message.message_id)   



    def info_boss(self, result):
        mensaje = result.replace('[', '')
        mensaje = mensaje.replace(']', '')
        mensaje = mensaje.replace('{', '')
        mensaje = mensaje.replace('}', '')
        mensaje = mensaje.replace(',', '')
        mensaje = mensaje.replace(':', '')
        mensaje = mensaje.replace("'", '')
        mensaje = mensaje.split()
        final = "Nº: " + mensaje[1] + "\n"
        final += "Nombre: " + mensaje[3] + "\n"
        final += "Km para caramelo: " + mensaje[5] + "\n"
        final += "PC 100: " + mensaje[7] + '/' + mensaje[9] + '\n'
        
        return final