<?php

use Symfony\Component\DependencyInjection\Argument\RewindableGenerator;

// This file has been auto-generated by the Symfony Dependency Injection Component for internal use.
// Returns the public 'prestashop.adapter.product.command_handler.remove_all_associated_product_attachments_handler' shared service.

return $this->services['prestashop.adapter.product.command_handler.remove_all_associated_product_attachments_handler'] = new \PrestaShop\PrestaShop\Adapter\Product\CommandHandler\RemoveAllAssociatedProductAttachmentsHandler(${($_ = isset($this->services['prestashop.adapter.product.update.product_attachment_updater']) ? $this->services['prestashop.adapter.product.update.product_attachment_updater'] : $this->load('getPrestashop_Adapter_Product_Update_ProductAttachmentUpdaterService.php')) && false ?: '_'});
