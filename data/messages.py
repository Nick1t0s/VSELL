import os

class Messages:
    @staticmethod
    def chanel_message(model: str,
               used: str,
               cost: int,
               place: str,
               description: str,
               user_id: int):
        current_dir = os.path.dirname(os.path.abspath(__file__))

        with open(f"{current_dir}/chanel_message.html", encoding="UTF-8") as f:
            template = f.read()


        return template.format(model=model, used=used, cost=cost, place=place, description=description, user_id=user_id)

