<?php

use Symfony\Component\DependencyInjection\Argument\RewindableGenerator;

// This file has been auto-generated by the Symfony Dependency Injection Component for internal use.
// Returns the public 'prestashop.bundle.form.admin.configure.advanced_parameters.employee.employee' shared service.

$this->services['prestashop.bundle.form.admin.configure.advanced_parameters.employee.employee'] = $instance = new \PrestaShopBundle\Form\Admin\Configure\AdvancedParameters\Employee\EmployeeType(${($_ = isset($this->services['prestashop.core.form.choice_provider.all_languages']) ? $this->services['prestashop.core.form.choice_provider.all_languages'] : $this->load('getPrestashop_Core_Form_ChoiceProvider_AllLanguagesService.php')) && false ?: '_'}->getChoices(), ${($_ = isset($this->services['prestashop.core.form.choice_provider.accessible_tab']) ? $this->services['prestashop.core.form.choice_provider.accessible_tab'] : $this->load('getPrestashop_Core_Form_ChoiceProvider_AccessibleTabService.php')) && false ?: '_'}->getChoices(), ${($_ = isset($this->services['prestashop.core.form.choice_provider.profile']) ? $this->services['prestashop.core.form.choice_provider.profile'] : $this->load('getPrestashop_Core_Form_ChoiceProvider_ProfileService.php')) && false ?: '_'}->getChoices(), ${($_ = isset($this->services['prestashop.adapter.multistore_feature']) ? $this->services['prestashop.adapter.multistore_feature'] : $this->getPrestashop_Adapter_MultistoreFeatureService()) && false ?: '_'}->isActive(), ${($_ = isset($this->services['prestashop.adapter.employee.avatar_provider']) ? $this->services['prestashop.adapter.employee.avatar_provider'] : $this->load('getPrestashop_Adapter_Employee_AvatarProviderService.php')) && false ?: '_'}->getDefaultAvatarUrl());

$instance->setTranslator(${($_ = isset($this->services['translator']) ? $this->services['translator'] : $this->getTranslatorService()) && false ?: '_'});

return $instance;
