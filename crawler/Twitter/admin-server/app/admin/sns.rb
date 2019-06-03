ActiveAdmin.register Sns do
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
    index do
        selectable_column
        id_column
        column :content
        column :keyword do |obj|
            obj.keyword.word
        end
        column :p_date   
        column :created_at
        actions
    end


end
