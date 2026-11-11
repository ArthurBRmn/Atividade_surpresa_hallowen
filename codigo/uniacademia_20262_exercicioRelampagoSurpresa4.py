class Pessoa:
    def __init__(self):
        self.__nome = ""
    def set_nome(self, nome):
        self.__nome = nome
    def get_nome(self):
        return self.__nome

class Aluno(Pessoa):
    def __init__(self):
        Pessoa.__init__(self)
        self.__turmas = []
        self.__cursos = []
    def set_turmas(self, turmas):
        self.__turmas = turmas
    def get_turmas(self):
        return self.__turmas
    def matricular_turma(self, turma):
        self.__turmas.append(turma)
    def verificar_turma(self, turma):
        return turma in self.__turmas
    def desmatricular_turma(self, turma):
        self.__turmas.remove(turma)
    def set_cursos(self, cursos):
        self.__cursos = cursos
    def get_cursos(self):
        return self.__cursos
    def matricular_curso(self, curso):
        self.__cursos.append(curso)
    def verificar_curso(self, curso):
        return curso in self.__cursos
    def desmatricular_curso(self, curso):
        self.__cursos.remove(curso)

class Professor(Pessoa):
    def __init__(self):
        Pessoa.__init__(self)
        self.__turmas = []
    def set_turmas(self, turmas):
        self.__turmas = turmas
    def get_turmas(self):
        return self.__turmas
    def adicionar_turma(self, turma):
        if turma not in self.__turmas:
            self.__turmas.append(turma)
    def remover_turma(self, turma):
        if turma in self.__turmas:
            self.__turmas.remove(turma)
    def get_nomes_turmas(self):
        resultado = []
        for turma in self.__turmas:
            resultado.append(turma.get_nome())
        return resultado

class Disciplina:
    def __init__(self):
        self.__nome = ""
        self.__turmas = []
    def set_nome(self, nome):
        self.__nome = nome
    def get_nome(self):
        return self.__nome
    def set_turmas(self, turmas):
        self.__turmas = turmas
    def get_turmas(self):
        return self.__turmas
    def adicionar_turma(self, turma):
        if turma not in self.__turmas:
            self.__turmas.append(turma)
    def remover_turma(self, turma):
        if turma in self.__turmas:
            self.__turmas.remove(turma)

class Turma:
    def __init__(self):
        self.__nome = ""
        self.__professor = None
        self.__disciplina = None
        self.__alunos = []
    def set_nome(self, nome):
        self.__nome = nome
    def get_nome(self):
        return self.__nome
    def set_professor(self, professor):
        if self.__professor != None:
            self.__professor.remover_turma(self)
        self.__professor = professor
        if professor != None:
            professor.adicionar_turma(self)
    def get_professor(self):
        return self.__professor
    def get_nome_professor(self):
        return self.__professor.get_nome()
    def set_disciplina(self, disciplina):
        if self.__disciplina != None:
            self.__disciplina.remover_turma(self)
        self.__disciplina = disciplina
        if disciplina != None:
            disciplina.adicionar_turma(self)
    def get_disciplina(self):
        return self.__disciplina
    def get_nome_disciplina(self):
        return self.__disciplina.get_nome()
    def set_alunos(self, alunos):
        for aluno in self.__alunos:
            aluno.desmatricular_turma(self)
        self.__alunos = alunos
        for aluno in self.__alunos:
            aluno.matricular_turma(self)
    def get_alunos(self):
        return self.__alunos
    def matricular(self, aluno):
        self.__alunos.append(aluno)
        aluno.matricular_turma(self)
    def get_nomes_alunos(self):
        resultado = []
        for aluno in self.__alunos:
            resultado.append(aluno.get_nome())
        return resultado
    def verificar_aluno(self, aluno):
        return aluno in self.__alunos
    def desmatricular(self, aluno):
        self.__alunos.remove(aluno)
        aluno.desmatricular_turma(self)

class Curso:
    def __init__(self):
        self.__alunos = []
        self.__turmas = []
    def set_alunos(self, alunos):
        for aluno in self.__alunos:
            aluno.desmatricular_curso(self)
        self.__alunos = alunos
        for aluno in self.__alunos:
            aluno.matricular_curso(self)
    def get_alunos(self):
        return self.__alunos
    def matricular(self, aluno):
        self.__alunos.append(aluno)
        aluno.matricular_curso(self)
    def get_nomes_alunos(self):
        resultado = []
        for aluno in self.__alunos:
            resultado.append(aluno.get_nome())
        return resultado
    def verificar_aluno(self, aluno):
        return aluno in self.__alunos
    def desmatricular(self, aluno):
        self.__alunos.remove(aluno)
        aluno.desmatricular_curso(self)
    def set_turmas(self, turmas):
        self.__turmas = turmas
    def get_turmas(self):
        return self.__turmas
    def adicionar_turma(self, turma):
        self.__turmas.append(turma)
    def get_nomes_professores(self):
        resultado = []
        for turma in self.__turmas:
            nome = turma.get_nome_professor()
            if nome not in resultado:
                resultado.append(nome)
        return resultado
    def get_nomes_alunos_turmas(self):
        resultado = []
        for turma in self.__turmas:
            for nome in turma.get_nomes_alunos():
                resultado.append(nome)
        return resultado
    def get_nomes_disciplinas(self):
        resultado = []
        for turma in self.__turmas:
            nome = turma.get_nome_disciplina()
            if nome not in resultado:
                resultado.append(nome)
        return resultado
    def verificar_turma(self, turma):
        return turma in self.__turmas
    def desmatricular_turma(self, turma):
        self.__turmas.remove(turma)
