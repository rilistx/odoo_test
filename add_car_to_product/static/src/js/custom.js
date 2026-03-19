/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";
import { jsonrpc } from "@web/core/network/rpc_service";

publicWidget.registry.AutopartsFilter = publicWidget.Widget.extend({
    selector: '.autoparts_filter_form',

    events: {
        'change select[name="brand_id"]': '_onBrandChange',
    },

    start: function () {
        const brandId = this.$('select[name="brand_id"]').val();

        if (brandId) {
            this._loadModels(brandId);
        }

        return this._super.apply(this, arguments);
    },

    _onBrandChange: function (ev) {
        this._loadModels($(ev.target).val());
    },

    _loadModels: function (brandId) {
        const $modelSelect = this.$('select[name="model_id"]');
        const selectedModelId = $modelSelect.attr('data-selected-id') || $modelSelect.data('selected-id');

        $modelSelect.html('<option value="">Завантаження...</option>');

        if (!brandId) {
            $modelSelect.html('<option value="">Обрати модель</option>');
            return;
        }

        jsonrpc('/shop/get_models', {
            brand_id: parseInt(brandId),
        }).then((models) => {
            $modelSelect.html('<option value="">Обрати модель</option>');

            if (models && models.length > 0) {
                models.forEach(m => {
                    const isSelected = m.id == selectedModelId ? 'selected="selected"' : '';
                    $modelSelect.append(`<option value="${m.id}" ${isSelected}>${m.name}</option>`);
                });
            }
        });
    }
});
