<?php

// This file has been auto-generated by the Symfony Dependency Injection Component for internal use.

if (\class_exists(\ContainerXjp2xgk\appProdProjectContainer::class, false)) {
    // no-op
} elseif (!include __DIR__.'/ContainerXjp2xgk/appProdProjectContainer.php') {
    touch(__DIR__.'/ContainerXjp2xgk.legacy');

    return;
}

if (!\class_exists(appProdProjectContainer::class, false)) {
    \class_alias(\ContainerXjp2xgk\appProdProjectContainer::class, appProdProjectContainer::class, false);
}

return new \ContainerXjp2xgk\appProdProjectContainer([
    'container.build_hash' => 'Xjp2xgk',
    'container.build_id' => '33de7aaa',
    'container.build_time' => 1637191087,
], __DIR__.\DIRECTORY_SEPARATOR.'ContainerXjp2xgk');
