# -*- coding: utf-8 -*-
import zipfile

# Conteúdo do arquivo .bpm (BPM Bizagi) para o seu processo
bpm_content = """
<?xml version="1.0" encoding="UTF-8"?>
<bpm:BizagiProcess xmlns:bpm="http://www.bizagi.com/bpm" name="ProcessoPedidoDelivery">
    <bpm:Pools>
        <bpm:Pool name="Cliente">
            <bpm:Lane name="Cliente"/>
        </bpm:Pool>
        <bpm:Pool name="Sistema">
            <bpm:Lane name="Sistema"/>
        </bpm:Pool>
        <bpm:Pool name="Operador">
            <bpm:Lane name="Operador"/>
        </bpm:Pool>
        <bpm:Pool name="Admin/Gerente">
            <bpm:Lane name="Admin/Gerente"/>
        </bpm:Pool>
    </bpm:Pools>
    <bpm:Activities>
        <bpm:Activity id="VisualizarCardapio" name="Visualizar Cardápio"/>
        <bpm:Activity id="MontarCarrinho" name="Montar Carrinho"/>
        <bpm:Activity id="InserirDados" name="Inserir Dados de Contato e Entrega"/>
        <bpm:Activity id="ValidarPedido" name="Validar Pedido (Backend)"/>
        <bpm:Activity id="CriarPedido" name="Criar Pedido no Sistema"/>
        <bpm:Activity id="EmitirNewOrder" name="Emitir evento new_order"/>
        <bpm:Activity id="AceitarPedido" name="Aceitar Pedido (Em Preparo)"/>
        <bpm:Activity id="RejeitarPedido" name="Rejeitar Pedido (Enviar Motivo)"/>
        <bpm:Activity id="AtualizarProgresso" name="Atualizar Status até Entrega"/>
        <bpm:Activity id="EditarCardapio" name="Criar/Editar/Excluir Itens"/>
        <bpm:Activity id="SalvarCardapio" name="Salvar Alterações"/>
    </bpm:Activities>
</bpm:BizagiProcess>
"""

# Nome do arquivo .bpm
bpm_filename = "ProcessoPedidoDelivery.bpm"

# Criar o arquivo .bpm
with open(bpm_filename, "w", encoding="utf-8") as f:
    f.write(bpm_content)

print(f"Arquivo '{bpm_filename}' criado com sucesso! Abra no Bizagi Modeler.")
