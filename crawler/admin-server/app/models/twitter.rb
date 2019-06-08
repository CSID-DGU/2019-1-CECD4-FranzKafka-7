class Twitter < ApplicationRecord
    belongs_to :keyword
    validates_uniqueness_of :item_id
    require 'activerecord-import/active_record/adapters/mysql2_adapter'

    def self.json_insert(file, keyword_id, valid_flag)
        p 'start insert'
        
        old_logger = ActiveRecord::Base.logger
        ActiveRecord::Base.logger = nil
        
        json = JSON.parse(file)
        
        size = json.size

        puts "size : "+size.to_s 

        tweets = []

        json.each_with_index do |j,i|
            j["item_id"] = j.delete("id")

            
            # if tweets.pluck(:item_id).include? j["item_id"]
            #     next
            # end
            
            j.delete("html")
            j.delete("url")
            p_date = DateTime.parse(j.delete("timestamp")).in_time_zone('Asia/Seoul')
            j["content"] = j.delete("text")
            j["name"] = j.delete("user")
            j["keyword_id"] = keyword_id
            j["p_date"] = p_date
            tweets << Twitter.new(j)
            
            if i%1000 == 0 or i == size-1
                begin
                    puts i.to_s+"개 까지 함"
                    if valid_flag == true
                        Twitter.import tweets, validate_uniqueness: true
                    else
                        Twitter.import tweets
                    end
                    tweets = []
                rescue Exception => e
                    p e.message
                    next
                end
            end
        end
        ActiveRecord::Base.logger = old_logger
    end
end
