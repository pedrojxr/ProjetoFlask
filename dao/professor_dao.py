from dao.db_config  import get_connection 

class ProfessorDAO: 

    sqlSelect = 'SELECT id, nome, disciplina FROM professor'

    def listar(self): 
        conn = get_connection() 
        cursor = conn.cursor() 
        cursor.execute(self.sqlSelect) 
        lista = cursor.fetchall() 
        conn.close() 
        return lista
    
    def salvar(self, nome, disciplina, id=None):
        conn = get_connection()
        cursor = conn.cursor()
        try:            
            if id:
                cursor.execute('UPDATE professor SET nome = %s, disciplina =%s WHERE id =%s', (nome, disciplina, id))
            else:
                cursor.execute('INSERT INTO professor (nome, disciplina) VALUES (%s, %s)', (nome, disciplina))
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}
        finally:
            conn.close()
            
    def procurar_por_id(self, id):
        conn = get_connection() 
        cursor = conn.cursor() 
        cursor.execute('SELECT id, nome, disciplina FROM professor WHERE id = %s', (id,))
        record = cursor.fetchone()
        conn.close()
        return record
    
    def remover(self, id):
        conn = get_connection() 
        cursor = conn.cursor() 
        try:
            cursor.execute('DELETE FROM professor WHERE id = %s', (id,))
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}
        finally:
            conn.close()