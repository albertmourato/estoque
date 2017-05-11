import string
from behave import *
from django.contrib import messages

#  Scenario: Cadastrar valor para item que não está disponível na loja escolhido - GUI
@given('Eu estou na pagina de cadastramento de precos')
	def step_impl(context):
	    br = context.browser
	    br.visit(context.new_price_url)
	    response = br.status_code
	    assert response.code == 200
	    assert br.url.endswith("/newItem/")

@given('eu vejo o item "{it}" na lista de itens cadastrados')
	def step_impl(context):
		br = context.browser
		Controller.newItem(it)
		itemList = br.find_by_id('itemList')
		assert itemList.get(name = it) != null

@given('eu vejo a loja "{it}" na lista de lojas cadastradas')
	def step_impl(context):
		br = context.browser
		Controller.newStore(it)
		storeList = br.find_by_id('storeList')
		assert storeList.get(name = it) != null

@given('a loja "{loja}" nao possui o item "{item}"')
	def step_impl(context):
		br = context.browser
		itemList = br.find_by_id('itemList')
		storeList = br.find_by_id('storeList')
		it = itemList.get(name = item)
		st = storeList.get(name = loja)
		assert !(controller.verifyIteminStore(it, st))

@when('eu tento cadastrar o preco "{preco}" do item "{item}" na loja "{loja}"')
	def step_impl(context):
		br = context.browser
		itemList = br.find_by_id('itemList')
		storeList = br.find_by_id('storeList')
		editText = br.find_by_id('editText')
		it = itemList.get(name = item)
		st = storeList.get(name = loja)
		it.select()
		st.select()
		editText.fill(preco)
		button = br.find_by_id('createPrice')
		button.click()

@then('eu vejo uma mensagem informando que a loja "{loja}" nao possui o item "{item}"')
	def step_impl(context): 
		Controller.showException(["pt-br", "A loja "+loja+" não possui o item "+item])

@then('eu permaneco na pagina de cadastramento de precos')
	def step_impl(context): 
		br = context.browser
	    response = br.status_code
	    assert response.code == 200
	    assert br.url.endswith("/newPrice/")
