<?php

use Twig\Environment;
use Twig\Error\LoaderError;
use Twig\Error\RuntimeError;
use Twig\Markup;
use Twig\Sandbox\SecurityError;
use Twig\Sandbox\SecurityNotAllowedTagError;
use Twig\Sandbox\SecurityNotAllowedFilterError;
use Twig\Sandbox\SecurityNotAllowedFunctionError;
use Twig\Source;
use Twig\Template;

/* C:\Program Files (x86)\EasyPHP-Devserver-17\eds-www\prestashop\mails\themes\classic\core\test.html.twig */
class __TwigTemplate_170c7fa6e2a92d7a60141af67b3fa82c92f0b81b3a708a16add766865b62f113 extends \Twig\Template
{
    public function __construct(Environment $env)
    {
        parent::__construct($env);

        $this->blocks = [
            'content' => [$this, 'block_content'],
        ];
    }

    protected function doGetParent(array $context)
    {
        // line 1
        return "@MailThemes/classic/components/layout.html.twig";
    }

    protected function doDisplay(array $context, array $blocks = [])
    {
        $this->parent = $this->loadTemplate("@MailThemes/classic/components/layout.html.twig", "C:\\Program Files (x86)\\EasyPHP-Devserver-17\\eds-www\\prestashop\\mails\\themes\\classic\\core\\test.html.twig", 1);
        $this->parent->display($context, array_merge($this->blocks, $blocks));
    }

    // line 3
    public function block_content($context, array $blocks = [])
    {
        // line 4
        echo "<tr>
  <td align=\"center\" class=\"titleblock\">
    <span class=\"title\">";
        // line 6
        echo $this->env->getExtension('Symfony\Bridge\Twig\Extension\TranslationExtension')->trans("Hello", [], "Emails.Body", ($context["locale"] ?? null));
        echo "</span>
  </td>
</tr>
<tr>
  <td class=\"space_footer\">&nbsp;</td>
</tr>
<tr>
  <td class=\"linkbelow\">
    <span>
      ";
        // line 15
        echo $this->env->getExtension('Symfony\Bridge\Twig\Extension\TranslationExtension')->trans("This is a [1]test e-mail[/1] from your shop.", ["[1]" => "<span><strong>", "[/1]" => "</strong></span>"], "Emails.Body", ($context["locale"] ?? null));
        echo ".
      <br/><br/>
      ";
        // line 17
        echo $this->env->getExtension('Symfony\Bridge\Twig\Extension\TranslationExtension')->trans("If you can read this, the test was successful!", [], "Emails.Body", ($context["locale"] ?? null));
        echo ".
    </span>
  </td>
</tr>
";
    }

    public function getTemplateName()
    {
        return "C:\\Program Files (x86)\\EasyPHP-Devserver-17\\eds-www\\prestashop\\mails\\themes\\classic\\core\\test.html.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  63 => 17,  58 => 15,  46 => 6,  42 => 4,  39 => 3,  29 => 1,);
    }

    /** @deprecated since 1.27 (to be removed in 2.0). Use getSourceContext() instead */
    public function getSource()
    {
        @trigger_error('The '.__METHOD__.' method is deprecated since version 1.27 and will be removed in 2.0. Use getSourceContext() instead.', E_USER_DEPRECATED);

        return $this->getSourceContext()->getCode();
    }

    public function getSourceContext()
    {
        return new Source("", "C:\\Program Files (x86)\\EasyPHP-Devserver-17\\eds-www\\prestashop\\mails\\themes\\classic\\core\\test.html.twig", "C:/Program Files (x86)/EasyPHP-Devserver-17/eds-www/prestashop/mails/themes/classic/core/test.html.twig");
    }
}
