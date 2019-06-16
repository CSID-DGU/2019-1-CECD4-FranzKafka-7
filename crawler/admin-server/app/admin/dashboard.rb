ActiveAdmin.register_page "Dashboard" do
  menu priority: 1, label: proc { I18n.t("active_admin.dashboard") }

    content title: proc{ I18n.t("active_admin.dashboard") } do
    # div class: "blank_slate_container", id: "dashboard_default_message" do
    #   span class: "blank_slate" do
    #     span I18n.t("active_admin.dashboard_welcome.welcome")
    #     small I18n.t("active_admin.dashboard_welcome.call_to_action")
    #   end
    # end

    # Here is an example of a simple dashboard with columns and panels.
    #
    div '지진'
    div 'Twitter : ' + Twitter.where(keyword: 1).count.to_s + '개'
    div 'DcInside : ' + Dcinside.count.to_s + '개'
    div '산불'
    div 'Twitter : ' + Twitter.where(keyword: 2).count.to_s + '개'    

    columns do
      panel "Twitter Data" do
        render 'line_chart',  {model_name: 'twitters'}
        # div "Total : #{ImageInfo.count } 개 "
        # div "트립 : #{ImageInfo.where("trip_idx is not null").count } 개 "
        # div "인스타 : #{ImageInfo.where("insta_data_id is not null").count } 개"
      end
    end

    columns do      
      panel "DcInside Data",style:"" do
        render 'line_chart',  {model_name: 'dcinsides'}
      end
    end

  end # content




    # Here is an example of a simple dashboard with columns and panels.
    #
    # columns do
    #   column do
    #     panel "Recent Posts" do
    #       ul do
    #         Post.recent(5).map do |post|
    #           li link_to(post.title, admin_post_path(post))
    #         end
    #       end
    #     end
    #   end

    #   column do
    #     panel "Info" do
    #       para "Welcome to ActiveAdmin."
    #     end
    #   end
    # end
  #end # content
end
