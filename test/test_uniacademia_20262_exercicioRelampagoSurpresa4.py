from codigo.uniacademia_20262_exercicioRelampagoSurpresa4 import *

def test_deve_retornar_alunos_curso():
    curso = Curso()
    aluno1 = Aluno()
    aluno2 = Aluno()
    curso.matricular(aluno1)
    curso.matricular(aluno2)
    assert curso.get_alunos() == [aluno1, aluno2]

def test_deve_retornar_nomes_alunos_curso():
    curso = Curso()
    aluno1 = Aluno()
    aluno1.set_nome("Lucas")
    aluno2 = Aluno()
    aluno2.set_nome("Rafael")
    curso.matricular(aluno1)
    curso.matricular(aluno2)
    assert curso.get_nomes_alunos() == ["Lucas", "Rafael"]

def test_deve_encontrar_aluno_curso():
    aluno = Aluno()
    curso = Curso()
    curso.matricular(aluno)
    assert curso.verificar_aluno(aluno) == True

def test_nao_deve_encontrar_aluno_curso():
    aluno = Aluno()
    curso = Curso()
    assert curso.verificar_aluno(aluno) == False

def test_deve_remover_aluno_curso():
    aluno = Aluno()
    curso = Curso()
    curso.matricular(aluno)
    curso.desmatricular(aluno)
    assert curso.get_alunos() == []