class Dcinside < ApplicationRecord
    belongs_to :keyword
    validates_uniqueness_of :post_no

    require 'activerecord-import/active_record/adapters/mysql2_adapter'
    def self.json_insert(file, keyword_id, valid_flag)
        p 'start insert'
        
        old_logger = ActiveRecord::Base.logger
        ActiveRecord::Base.logger = nil
        
        json = JSON.parse(file)
        
        size = json.size

        puts "size : "+size.to_s 

        galls = []

        json.each_with_index do |j,i|

            
            if galls.pluck(:post_no).include? j["post_no"]
                next
            end
            j.delete("crawled_at")
            written_at = DateTime.parse(j.delete("written_at")+" +09:00")
            j["keyword_id"] = keyword_id
            j["written_at"] = written_at
            galls << Dcinside.new(j)
            
            if i%1000 == 0 or i == size-1
                begin
                    puts i.to_s+"개 까지 함"
                    if valid_flag == true
                        Dcinside.import galls, validate_uniqueness: true
                    else
                        Dcinside.import galls
                    end
                    galls = []
                rescue Exception => e
                    p e.message
                    next
                end
            end
        end
        ActiveRecord::Base.logger = old_logger
    end

end
