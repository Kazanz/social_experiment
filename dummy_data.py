from datetime import datetime, timedelta
from random import randint, shuffle

from faker import Factory

from positive_affirmation.users.models import User, Affirmation


AFFIRMATIONS = [
    "Happiness is my birthright. I embrace happiness as my set point state of being.",
    "I feel joy and contentment in this moment right now.",
    "I awaken in the morning feeling happy and enthusiastic about life.",
    "I can tap into a wellspring of inner happiness anytime I wish.",
    "By allowing myself to be happy, I inspire others to be happy as well.",
    "I have fun with all of my endeavors, even the most mundane.",
    "I look at the world around me and can't help but smile and feel joy.",
    "I find joy and pleasure in the most simple things in life.",
    "I have an active sense of humor and love to share laughter with others.",
    "My heart is overflowing with joy.",
    "I rest in happiness when I go to sleep, knowing all is well in my world.",
    "My partner and I share a deep and powerful love for each other.",
    "I respect and admire my partner and see the best in him/her.",
    "I love my partner exactly how he/she is and enjoy his/her unique qualities.",
    "My partner and I share emotional intimacy daily through talking and touch.",
    "I have healthy boundaries with my partner.",
    "My partner and I have fun together and find new ways to enjoy our time together.",
    "My partner and I communicate openly and resolve conflict peacefully and respectfully.",
    "I am able to be fully myself and completely authentic in my love relationship.",
    " I communicate my desires and needs clearly and confidently with my partner.",
    "I want the best for my partner and easily go out of my way to support him/her.",
    "I expect to be successful in all of my endeavors. Success is my natural state.",
    "I easily find solutions to challenges and roadblocks and move past them quickly.",
    "Mistakes and setbacks are stepping stones to my success because I learn from them.",
    "Every day in every way, I am becoming more and more successful.",
    "I feel successful with my life right now, even as I work toward future success.",
    "I know exactly what I need to do to achieve success.",
    "I see fear as the fuel for my success and take bold action in spite of fear.",
    "I feel powerful, capable, confident, energetic, and on top of the world.",
    "I have an intention for success and know it is a reality awaiting my arrival.",
    "I have now reached my goal of _______ and feel the excitement of my achievement.",
    "Today I am successful. Tomorrow I will be successful. Every day I am successful.",
    "When I breath, I inhale confidence and exhale timidity.",
    "I love meeting strangers and approach them with boldness and enthusiasm.",
    "I live in the present and am confident of the future.",
    "My personality exudes confidence. I am bold and outgoing.",
    "I am self-reliant, creative and persistent in whatever I do.",
    "I am energetic and enthusiastic. Confidence is my second nature.",
    "I always attract only the best of circumstances and the best positive people in my life.",
    "I am a problem solver. I focus on solutions and always find the best solution.",
    "I love change and easily adjust myself to new situations.",
    "I am well groomed, healthy and full of confidence. My outer self is matched by my inner well being.",
    "Self confidence is what I thrive on. Nothing is impossible and life is great.",
    "I always see only the good in others. I attract only positive confident people.",
    "I approve of myself and love myself deeply and completely.",
    "I am unique. I feel good about being alive and being me.",
    "I trust myself and know my inner wisdom is my best guide.",
    "I have integrity. I am totally reliable. I do what I say.",
    "I act from a place of personal security.",
    "I fully accept myself and know that I am worthy of great things in life.",
    "I choose to be proud of myself.",
    "I find deep inner peace within myself as I am.",
    "I fill my mind with positive and nourishing thoughts.",
    "My confidence, self esteem, and inner wisdom are increasing with each day.",
    "My immune system is very strong and can deal with any kind of bacteria, germs and viruses.",
    "Every cell in my body vibrates with energy and health.",
    "I am completely pain free, and my body is full of energy.",
    "I nourish my body with healthy food.",
    "All of my body systems are functioning perfectly..",
    "My body is healing, and I feel better and better every day.",
    "I enjoy exercising my body and strengthening my muscles.",
    "With every breath out, I release stress in my body.",
    "I send love and healing to every organ of my body.",
    "I breathe deeply, exercise regularly and feed only good nutritious food to my body.",
    "I pay attention and listen to what my body needs for health and vitality.",
    "I sleep soundly and peacefully, and awaken feeling rested and energetic.",
    "I am surrounded by people who encourage and support healthy choices.",
    "My world is a peaceful, loving, and joy-filled place to live.",
    "I sow the seeds of peace wherever I go.",
    "I surround myself with peaceful people.",
    "My work environment is calm and peaceful.",
    "I breath in peace, I breath out chaos and disorder.",
    "My home is a peaceful sanctuary where I feel safe and happy.",
    "In all that I say and do, I choose peace.",
    "I release past anger and hurts and fill myself with serenity and peaceful thoughts.",
    "Peace descends all around me now and always.",
    "I send peace from myself into the world.",
    "I respond peacefully in all situations.",
    "I am grounded in the experience of the present moment.",
    "I am focus and engaged in the task at hand.",
    "All is well right now.",
    "I am grateful for this moment and find joy in it.",
    "I gently and easily return to the present moment.",
    "I observe my thoughts and actions without judging them.",
    "I am fully present in all of my relationships.",
    "Life is happening in this moment.",
    "I accept and embrace all experiences, even unpleasant ones.",
    "I observe my emotions without getting attached to them.",
    "I meditate easily without resistance or anxiety.",
    "I release the past and live fully in the present moment.",
    "Calmness washes over me with every deep breath I take.",
    "Every day I am more and more at ease.",
    "Being calm and relaxed energizes my whole being.",
    "All the muscles in my body are releasing and relaxing.",
    "All negativity and stress are evaporating from my body and my mind.",
    "I breath in relaxation. I breath out stress.",
    "Even when there is chaos around me, I remain calm and centered.",
    "I transcend stress of any kind. I live in peace.",
    "I am free of anxiety, and a calm inner peace fills my mind and body.",
    "All is well in my world. I am calm, happy, and content.",
]
shuffle(AFFIRMATIONS)

fake = Factory.create()


def create_dummies():
    for _ in range(0, 9):
        user = User.objects.create(username=fake.user_name(),
                                   password=fake.password(),
                                   dummy_user=True, control=False)
    users = [u for u in User.objects.filter(dummy_user=True).all()]
    for i in range(0, len(AFFIRMATIONS)-1):
        shuffle(users)
        user = users[i % 9]
        Affirmation.objects.create(user=user, text=AFFIRMATIONS[i])


if __name__ == "__main__":
    create_dummies()
