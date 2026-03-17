def solution(genres, plays):
    genre_total = {}
    genre_songs = {}
    
    for i, (genre, play) in enumerate(zip(genres, plays)):
        genre_total[genre] = genre_total.get(genre, 0) + play
        
        if genre not in genre_songs:
            genre_songs[genre] = []
        
        genre_songs[genre].append((play, i))
        
    sorted_genres = sorted(genre_total.keys(), key=lambda x: genre_total[x], reverse=True)
    
    answer = []
    
    for genre in sorted_genres:
        songs = sorted(genre_songs[genre], key=lambda x: (-x[0], x[1]))
        for play, idx in songs[:2]:
            answer.append(idx)
            
    return answer