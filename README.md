# Pytest - Framework de Testes Python
Pytest é um framework para testes de software, por linha de comando, que automaticamente encontra os testes de um diretório, roda os testes e reporta os resultados. Por ser extendido com plugins próprios ou de teceriros.
Algumas características:
- Os testes são escritos de forma bem simpels. Até mesmo testes que são complexos.
- Testes são fáceis de ler.
- Inicia com muita rapidez.
- Usa assert (keyword python) para as verificações e não algo como self.assertLessThan().
- Possui uma grande comunidade que mantem o código.

## Um primeiro teste

```python
# test_001.py
def test_should_assert_when_equal_tuples():
    assert (1, 2) == (1, 2)
```

Neste primeiro teste, algumas coisas podem ser observadas no exemplo acima:
- O testes, para serem encontrados pelo Test Discovery do pytest, precisam iniciar com test_ no nome da função ou método e estar em um arquivo com test_ no início do nome.
- Quando o teste iniciar, a declaração assert determinará se o teste passa ou falha. Essa declaração é um palavra reservada do Pyhton que dispara uma exception AssertionError caso resulte em falso. Qualquer exception não tratada irá fazer com que o teste falhe.

## Instalação pytest

```shell
$ pip install pytest
```

## Rodando o teste
```shell
$ pytest test_001.py
```

```shell
================== test session starts ==================
collected 1 item              

tests/test_001_.py .          [100%]

================== 1 passed in 0.01s ==================
```

O ponto depois de tests/test_001_.py significa que um teste rodou e passou. A [100%] como porcentagem indica o progresso de testes rodados. Se quisermos mais informações sobre a execução, podemos rodar o mesmo comando passando o -v ou --verbose:

```shell
$ pytest -v test_001.py
```
```shell
=============== test session starts ===============
collected 1 item                                                  

tests/test_001_.py::test_should_assert_when_equal_tuples PASSED   [100%]

=============== 1 passed in 0.01s ===============

```

Caso o teste falhasse, teríamos:
```python
# test_001.py
def test_should_assert_when_equal_tuples():
    assert (2, 1) == (1, 2)
```
```shell
$ pytest test_001.py
```
```shell
====================================== test session starts ======================================
collected 1 item                                                                                

tests/test_001_.py F                                                                      [100%]

=========================================== FAILURES ============================================
_____________________________ test_should_assert_when_equal_tuples ______________________________

    def test_should_assert_when_equal_tuples():
>       assert (2, 1) == (1, 2)
E       assert (2, 1) == (1, 2)
E         At index 0 diff: 2 != 1
E         Use -v to get more diff

tests/test_001_.py:2: AssertionError
==================================== short test summary info ====================================
FAILED tests/test_001_.py::test_should_assert_when_equal_tuples - assert (2, 1) == (1, 2)
======================================= 1 failed in 0.07s =======================================
```

Com um pouco mais de detalhes:
```shell
$ pytest -v test_001.py
```
```shell
=============================== test session starts ===============================
collected 1 item                                                                  

test_001.py::test_should_assert_when_equal_tuples FAILED                    [100%]

==================================== FAILURES =====================================
______________________ test_should_assert_when_equal_tuples _______________________

    def test_should_assert_when_equal_tuples():
>       assert (2, 1, 3) == (3, 2, 1)
E       assert (2, 1, 3) == (3, 2, 1)
E         At index 0 diff: 2 != 3
E         Full diff:
E         - (3, 2, 1)
E         + (2, 1, 3)

test_001.py:2: AssertionError
============================= short test summary info =============================
FAILED test_001.py::test_should_assert_when_equal_tuples - assert (2, 1, 3) == (...
================================ 1 failed in 0.08s ================================

```

## Test Discovery

Test Discovery é a parte do pytest que procura pro testes dentro de um diretório e subdiretórios, caso o caminho do teste não esteja explícito no comando.

Para encontrar os testes é necessário:
- O nome dos arquivos devem ser nomeados com test_<nome>.py ou <nome>_test.py
- Os métodos e funções que testam devem começar com test_<nome>
- O nome das classes devem começar com Test<nome>

# Escrevendo testes

Dado um projeto de manipulação de cards, podemos gerar alguns testes afim de garantir algumas ações fundamentais para o bom funcionamento do código:

```python
@dataclass
class Card:
    summary: str = None
    owner: str = None
    state: str = "todo"
    id: int = field(default=None, compare=False)

    @classmethod
    def from_dict(cls, d):
        return Card(**d)
    def to_dict(self):
        return asdict(self)
```
```python
def test_from_dict_should_create_valid_card_object():
    c1 = Card(
        'something',
        'Brian',
        'todo',
        123
    )

    card_dict = {
        'summary': 'something',
        'owner': 'Brian',
        'state': 'todo',
        'id': 123
    }

    c2 = Card.from_dict(card_dict)

    assert c1 == c2
```
```shell
$ pytest
```
```shell
======================================== test session starts ========================================
collected 4 items                                                                                   

tests/test_001.py .                                                                           [ 25%]
tests/test_002.py ...                                                                         [100%]

========================================= 4 passed in 0.05s =========================================
```
Podemos ter ainda mais detalhes do teste adicionando -vv ao comando:

```python
def test_equality_should_fail():
    c1 = Card(
        'something',
        'Brian',
        'todo',
        123
    )
    c2 = Card(
        'something',
        'Bob',
        'todo',
        123
    )

    assert c1 == c2
```
```shell
$ pytest -vv
```
```shell
======================================== test session starts ========================================
collected 5 items                                                                                   

tests/test_001.py::test_should_assert_when_equal_tuples PASSED                                [ 20%]
tests/test_002.py::test_card_should_create_cards_object_successfully PASSED                   [ 40%]
tests/test_002.py::test_from_dict_should_create_valid_card_object PASSED                      [ 60%]
tests/test_002.py::test_to_dict_should_return_valid_dict PASSED                               [ 80%]
tests/test_002.py::test_equality_should_fail FAILED                                           [100%]

============================================= FAILURES ==============================================
_____________________________________ test_equality_should_fail _____________________________________

    def test_equality_should_fail():
        c1 = Card(
            'something',
            'Brian',
            'todo',
            123
        )
        c2 = Card(
            'something',
            'Bob',
            'todo',
            123
        )
    
>       assert c1 == c2
E       AssertionError: assert Card(summary='something', owner='Brian', state='todo', id=123) == Card(summary='something', owner='Bob', state='todo', id=123)
E         
E         Matching attributes:
E         ['summary', 'state']
E         Differing attributes:
E         ['owner']
E         
E         Drill down into differing attribute owner:
E           owner: 'Brian' != 'Bob'
E           - Bob
E           + Brian

tests/test_002.py:72: AssertionError
====================================== short test summary info ======================================
FAILED tests/test_002.py::test_equality_should_fail - AssertionError: assert Card(summary='somethi...
==================================== 1 failed, 4 passed in 0.13s ====================================
```

## Algumas expressoes assert
- assert something
- assert not someting
- assert a == b
- assert a != b
- assert a is None
- assert a is not None
- assert a <= b

## Controlando falha nos testes

É comum querer garantir que uma exception é lançada no código caso alguma coisa esteja fora do modo que deveria. Nesses casos, precisamos usar a funçãop pytest.raises(). Ela aguarda uma exception específica e faz o teste passar, caso seja a exception esperada.
```python
def test_equality_should_fail():

    c1 = Card(
        'something',
        'Brian',
        'todo',
        123
    )
    c2 = Card(
        'something',
        'Bob',
        'todo',
        123
    )

    with pytest.raises(AssertionError):
        assert c1 == c2
```

## Agrupando testes com classes

Podemos criar classes de testes que agrupam e organizam os testes de forma bem simples:

```python
class TestCardsobject:
    def test_card_should_create_cards_object_successfully(self):
        c = Card(
            'something',
            'Brian',
            'todo',
            123
        )

        assert c.summary == 'something'
        assert c.owner == 'Brian'
        assert c.state == 'todo'
        assert c.id == 123
```
```shell
$ pytest
```
```shell
======================================== test session starts ========================================
platform darwin -- Python 3.9.5, pytest-7.1.3, pluggy-1.0.0
rootdir: /Users/gabriel/projetos/pytest_minibev
plugins: anyio-3.6.1
collected 8 items                                                                                   

tests/test_001.py .                                                                           [ 12%]
tests/test_002.py ....                                                                        [ 62%]
tests/test_003.py ...                                                                         [100%]

========================================= 8 passed in 0.06s =========================================
```

## Rodando subset de testes

Podemos informar não apenas um ou mais arquivos que queremos executar o teste, mas também podemos informar quais partes dos testes que queremos rodar. Isso pode ser bem útil quando temos muitos testes e não queremos rodar toda a suite sempre:

- Um único método de dentro de uma classe -> pytest path/test_module.py::TestClass::test_method
- Todos os testes de uma classe -> pytest path/test_module.py::TestClass
- Uma única função -> pytest path/test_module.py::test_function

Outra forma é utilizando o parâmetro -k passando uma palavra para filtrar pelo nome:
```shell
$ pytest -k create_valid_card_object
```
```shell
======================================== test session starts ========================================
platform darwin -- Python 3.9.5, pytest-7.1.3, pluggy-1.0.0
rootdir: /Users/gabriel/projetos/pytest_minibev
plugins: anyio-3.6.1
collected 8 items / 6 deselected / 2 selected                                                       

tests/test_002.py .                                                                           [ 50%]
tests/test_003.py .                                                                           [100%]

================================== 2 passed, 6 deselected in 0.06s ==================================
```

No caso acima, ele executou apenas 2 testes pois eles coincidiram com o nome que colocamos no filtro.

# Fixtures

Fixtures são funções executadas antes do teste iniciar. Elas podem servir para preparar um conjunto de dados para o teste em questão, por exemplo.

## Adicionando uma fixture ao teste
```python
@pytest.fixture
def card_data():
    return {
        'summary': 'something',
        'owner': 'Brian',
        'state': 'todo',
        'id': 123
    }
```

Neste caso, adicionamos uma função e decoramos com pytest.fixture(). Para usarmos essa fixture, precisamos apenas adicionar o nome dela nos parâmetros das funções.

```python
def test_from_dict_should_create_valid_card_object(card_data):
    c1 = Card(
        'something',
        'Brian',
        'todo',
        123
    )

    c2 = Card.from_dict(card_data)

    assert c1 == c2
```

Essa fixture pode ser usada por qualquer outro teste e sempre terá o mesmo retorno para todos eles.
É possível também adicionarmos a fixture dentro de estruturas de classes, mas neste caso ela ficará disponível apenas para os métodos do mesmo escopo.

```python
class TestCardsobject:

    @pytest.fixture
    def card_data(self):
        return {
            'summary': 'something',
            'owner': 'Brian',
            'state': 'todo',
            'id': 123
        }

    def test_to_dict_should_return_valid_dict(self, card_data):
        c1 = Card(
            'something',
            'Brian',
            'todo',
            123
        )

        c2 = c1.to_dict()

        assert c2 == card_data
```

## Compartilhando fixtures entre arquivos

As fixtures podem também serem compartilhadas entre arquivos diferentes. Neste caso, devemo usar o arquivo com o nome conftest.py.

```python
# tests/conftest.py
import pytest

from cards_proj.src.cards.api import Card


@pytest.fixture
def card_object():
    return Card(
        'something',
        'Brian',
        'todo',
        123
    )
```
```python
# tests/test_005
def test_to_dict_should_return_valid_dict(self, card_data, card_object):
    c2 = card_object.to_dict()

    assert c2 == card_data
```

Podemos ver as fixtures usadas passando a flag --setup-show

```shell
$ pytest --setup-show test_005.py
```
```shell
======================================== test session starts =========================================
collected 3 items                                                                                    

tests/test_005.py 
        tests/test_005.py::TestCardsobject::test_card_should_create_cards_object_successfully.
        tests/test_005.py::TestCardsobject::test_from_dict_should_create_valid_card_object.
        SETUP    F card_data
        SETUP    F card_object
        tests/test_005.py::TestCardsobject::test_to_dict_should_return_valid_dict (fixtures used: card_data, card_object).
        TEARDOWN F card_object
        TEARDOWN F card_data

```

## Encontrando onde as fixtures foram definidas
Os arquivos de conftest.py não são limitados em apenas um para todo o diretório de testes. Cada nível de diretório pode ter um e eles sempre se sobrescrevem quando o nome da fixture coincide. Isso pode gerar um problema já que, a medida que os testes crescem no projeto, pode se tornar difícil encontrar um fixture específica.

Para resolver, podemos usar o comando com a flag --fixtures -v. O pytest exibirá uma lista de fixtures que estão disponíveis:

```shell
$ pytest --fixtures -v
```
```shell
======================================== test session starts =========================================

collected 15 items

...

-------------------------------- fixtures defined from tests.conftest --------------------------------
card_object -- tests/conftest.py:7
    no docstring available


-------------------------------- fixtures defined from tests.test_004 --------------------------------
card_data -- tests/test_004.py:7
    no docstring available


-------------------------------- fixtures defined from tests.test_005 --------------------------------
card_data -- tests/test_005.py:9
    no docstring available


======================================= no tests ran in 0.03s ========================================
```


# Parametrização

A parametrização permite que sejam passados um ou mais valores que serão testados dentro de uma única função em loop. Permite que possamos aproveitar melhor os testes criados com novos cenários, sem ter que escrever mais código para isso.
## Parametrizando funções

Iremos utilizar a função parametrize decoradas nas funções para criarmos listas de valores que serão executados um por vez, evitando assim que muitos testes iguais sejam cridos:

```python
@pytest.mark.parametrize(
    'exception', [
        OrganizationNotFoundException,
        DatabaseError,
        Exception
    ]
)
async def test_should_raise_exception_when_fail_to_create_distribution_center(  # noqa
    self,
    exception,
    seller_name,
    external_id,
    organization_name,
    mock_create_distribution_center,
    mock_create_service,
):
    mock_create_distribution_center.side_effect = (
        exception
    )

    with pytest.raises(exception):
        await create_distribution_center_with_default_service(
            seller_name=seller_name,
            organization_name=organization_name,
            external_id=external_id
        )
```

Abaixo, um exemplo com mais de um parâmetro que é esperado dentro da função:

```python
@pytest.mark.parametrize(
    'initial_time, final_time',
    [
        ('12:00:00', '11:00:00'),
        ('12:00:00', '12:00:00'),
    ]
)
def test_should_raise_validation_error_when_time_is_invalid(
    self,
    initial_time,
    final_time,
    service_cut_off
):
    service_cut_off['time']['initial'] = initial_time
    service_cut_off['time']['final'] = final_time

    with pytest.raises(ValidationError):
        CutOffSerializer().load(service_cut_off)
```
# Mock

Os mocks são substitutos dos objetos originais que imitam seu comportamento. Serve para controlarmos o comportamento do objeto em tempo de execução dos testes. Normalmente é usado para substituir chamadas de dependencias.


Iremos usar uma biblioteca padrão do python para manipular esses objetos
```python
from unittest import mock
```

MagicMock é uma classe especial que permite manipular qualquer retorno e comportamento conforme são acessados. Podemos configurá-las para especificar valores que queremos retornar:

```python
from unittest.mock import MagicMock

>>> thing = ProductionClass()
>>> thing.method = MagicMock(return_value=3)
>>> thing.method(3, 4, 5, key='value')
3
```

Neste exemplo, estamos criando um objeto MagicMock, passando o valor de retorno. Ao chamar o método, ele retorna o valor 3, pois configuramos eles já na criação do MagicMock().

```python
>>> mock = Mock(side_effect=KeyError('foo'))
>>> mock()
Traceback (most recent call last):
 ...
KeyError: 'foo'
```

No caso acima, utilizamos o side_effect que permite que uma exception seja disparada quando um método o atributo for chamado.

## Substituindo chamadas nos testes

Para que, em tempo de execução, o teste receba a chamada vinda de uma dependência mockada, precisamos informar o caminho ou o objeto que queremos mockar.

```python
# helpers.py
import lib.func_b


def func_a():
    print(func_b())
```

```python
>>> with mock.patch('helpers.lib.func_b') as mocked:
>>>    mocked.return_value = 10
>>>    func_a()
10
```

Acima, mockamos a função func_b() passando o caminho da chamada dentro de mock.patch(). Em tempo de executação, sempre que essa função for chamada, retornará o mesmo valor 10.

Também é possível especificar um objeto que será substituído sempre que for chamado em tempo de execução:

```python
>>> with mock.patch.object(Object, 'method') as mocked:
>>>    ...
``` 
Podemos também aproveitar esse método mockado e utilizar as funções de assert_ que garante que os métodos serão chamados de acordo com a necessidade:

### assert_called()
```python
>>> mock = Mock()
>>> mock.method()
<Mock name='mock.method()' id='...'>
>>> mock.method.assert_called()
```

### assert_called_with()

```python
>>> mock = Mock()
>>> mock.method(1, 2, 3, test='wow')
<Mock name='mock.method()' id='...'>
>>> mock.method.assert_called_with(1, 2, 3, test='wow')
```

### assert_called_once()

```python
>>> mock = Mock()
>>> mock.method()
<Mock name='mock.method()' id='...'>
>>> mock.method.assert_called_once()
>>> mock.method()
<Mock name='mock.method()' id='...'>
>>> mock.method.assert_called_once()
Traceback (most recent call last):
...
AssertionError: Expected 'method' to have been called once. Called 2 times.
```

### assert_called_once_with()

```python
>>> mock = Mock(return_value=None)
>>> mock('foo', bar='baz')
>>> mock.assert_called_once_with('foo', bar='baz')
>>> mock('other', bar='values')
>>> mock.assert_called_once_with('other', bar='values')
Traceback (most recent call last):
  ...
AssertionError: Expected 'mock' to be called once. Called 2 times.
```

### assert_not_called()

```python
>>> m = Mock()
>>> m.hello.assert_not_called()
>>> obj = m.hello()
>>> m.hello.assert_not_called()
Traceback (most recent call last):
  ...
AssertionError: Expected 'hello' to not have been called. Called 1 times.
```

# Menções honrosas

## Model Bakery
https://github.com/model-bakers/model_bakery

Permite criar objetos das models que temos no Django. Ajuda bastante em testes onde precisamos simular o comportamento dos registros no banco de dados.

## VCR
https://vcrpy.readthedocs.io/en/latest/

Registra na primeira vez todas as chamadas externas que fizermos nos testes. Registra isso em um arquivo e sempre que formos chamar de novo, ele faz a consulta direto no arquivo da resposta, como se fosse um log.

Isso faz com que o retorno que está sendo mockado seja exatamente igual a chamada original.
