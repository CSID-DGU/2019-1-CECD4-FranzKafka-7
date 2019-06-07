ActiveAdmin.register Twitter do
# See permitted parameters documentation:
# https://github.com/activeadmin/activeadmin/blob/master/docs/2-resource-customization.md#setting-up-strong-parameters
#
# permit_params :list, :of, :attributes, :on, :model
#
# or
#
# permit_params do
#   permitted = [:permitted, :attributes]
#   permitted << :other if params[:action] == 'create' && current_user.admin?
#   permitted
# end
    action_item :import_json, only: :index do
        render 'import'
    end

    collection_action :import, method: [:post] do
        keyword_id = params["keyword"]["id"]
        Twitter.json_insert(params[:file].read, keyword_id)
        redirect_to admin_twitters_path
    end
    index do
        selectable_column
        id_column
        column :fullname
        column :name
        column :item_id
        column :content
        column :keyword do |obj|
            obj.keyword.word
        end
        column :p_date
        column :created_at
        
        actions
    end

    filter :id
    filter :item_id
    filter :p_date

end
