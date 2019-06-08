class TwittersController < ApplicationController
    def months
        @months = Twitter.group_by_month(:p_date, format: "%s%3N").count.to_a
        render json: @months
    end
end
