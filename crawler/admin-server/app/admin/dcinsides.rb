ActiveAdmin.register Dcinside do
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
        valid_flag = params['valid'] == "1"
        
        Dcinside.json_insert(params[:file].read, keyword_id, valid_flag)
        redirect_to admin_dcinsides_path
    end
    index do
        selectable_column
        id_column
        # column :user_id
        column :nickname
        # column :user_ip
        column :post_no
        column :title
        column :body
        column :written_at
        column :keyword do |obj|
            obj.keyword.word
        end
        # column :comment_cnt
        # column :view_cnt
        # column :view_up
        # column :created_at        
        actions
    end

    filter :id
    filter :post_no
    filter :written_at
end
