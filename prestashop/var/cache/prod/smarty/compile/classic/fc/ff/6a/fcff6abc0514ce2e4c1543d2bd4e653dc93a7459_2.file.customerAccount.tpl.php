<?php
/* Smarty version 3.1.39, created on 2021-11-18 15:24:00
  from 'C:\Program Files (x86)\EasyPHP-Devserver-17\eds-www\prestashop\modules\psgdpr\views\templates\front\customerAccount.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.39',
  'unifunc' => 'content_6196620049a543_66206896',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    'fcff6abc0514ce2e4c1543d2bd4e653dc93a7459' => 
    array (
      0 => 'C:\\Program Files (x86)\\EasyPHP-Devserver-17\\eds-www\\prestashop\\modules\\psgdpr\\views\\templates\\front\\customerAccount.tpl',
      1 => 1637151901,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_6196620049a543_66206896 (Smarty_Internal_Template $_smarty_tpl) {
?>
<a class="col-lg-4 col-md-6 col-sm-6 col-xs-12" id="psgdpr-link" href="<?php echo htmlspecialchars($_smarty_tpl->tpl_vars['front_controller']->value, ENT_QUOTES, 'UTF-8');?>
">
    <span class="link-item">
        <i class="material-icons">account_box</i> <?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'GDPR - Personal data','mod'=>'psgdpr'),$_smarty_tpl ) );?>

    </span>
</a>
<?php }
}
