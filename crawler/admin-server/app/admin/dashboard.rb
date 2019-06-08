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
    
    columns do
      panel "Data Count" do
        render 'line_chart'
        # div "Total : #{ImageInfo.count } 개 "
        # div "트립 : #{ImageInfo.where("trip_idx is not null").count } 개 "
        # div "인스타 : #{ImageInfo.where("insta_data_id is not null").count } 개"
      end
    end
    columns do
      column do
        panel "Recent data",style:"" do
          
        #   table border:"0",cellspacing:"0", cellpadding:"0", id:"index_table_image_infos" ,class:"index_table index" do
        #     render "thead"
        #     tbody do
        #       ImageInfo.order("image_idx desc").limit(4).map do |img_info|
        #         tr class:"odd",id:"image_info_#{img_info.image_idx}" do
        #           td class:"col col-image_idx" do
        #             img_info.image_idx
        #           end
        #           td class:"col col-search_keyword" do
        #             img_info.search_keyword
        #           end
        #           td class:"col col-img_thumb" do
        #             img src:"#{img_info.image_url}",style:"height: 6em;max-witdh:10em;"
        #           end
        #           td class:"col col-similarity" do
        #             img_info.similarity
        #           end
        #           if !current_admin_user.nil?
        #             td class:"col col-status" do
        #               label class:"switch" do
        #                 render "toggle", id:img_info.image_idx, status:img_info.status
        #               end
        #             end
        #           end
        #         end
        #       end
        #     end
          end

        #SELECT FLOOR(age / 10) as age_range, COUNT(*)
        #FROM thing
        #GROUP BY FLOOR(age / 10) ORDER BY FLOOR(age / 10);
        #
        #
         panel "호에엥" do
           # pie_chart ImageInfo.group(:similarity).count
           # pie_chart ImageInfo.find_by_sql("select round(similarity,1) as si , count(*) from image_info group by si having not si=0.0;")
          #  origin_group = ImageInfo.group("round(similarity,1)").count.except(0.0)
          #  sorry_sim = ImageInfo.where("similarity = 0.60")
          #  # wow_s
          #  new_group=Hash.new
          #  new_group["0.1 .. 0.29"]=origin_group[0.1]+origin_group[0.2]
          #  new_group["0.3 .. 0.49"]=origin_group[0.4]+origin_group[0.3]
          #  new_group["0.5 .. 0.69"] = origin_group[0.6]+origin_group[0.5]
          #  new_group["0.7 .. 1.0"] = origin_group[0.7]+origin_group[0.8]+origin_group[0.9]+origin_group[1.0]

          #  pie_chart new_group

        end
      end
      column do
        panel "호ㅡ헤에에" do
        #   collec = ["판정 전","적합","부적합","","다운완료"]
        #   data = ImageInfo.group(:status).count.transform_keys{|key| collec[key]}
        #   bar_chart data, library:{pieSliceText: "value"}
        end
      end
    end

    columns do
      # panel "Log -   ( time:  #{ShowLog.last.time}  )",style:"background-color:#272935;color:#eff0ea" do
      #   div "#{ShowLog.last.log}".html_safe
      # end
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
