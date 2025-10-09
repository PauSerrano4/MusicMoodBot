"""
Spotify API Client for MusicMoodBot
Handles authentication and music recommendation requests
"""

import logging
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from typing import List, Dict, Any, Optional

logger = logging.getLogger(__name__)

class SpotifyClient:
    """Client for interacting with Spotify API."""
    
    def __init__(self, client_id: str, client_secret: str, redirect_uri: str):
        """
        Initialize Spotify client with credentials.
        
        Args:
            client_id: Spotify client ID
            client_secret: Spotify client secret
            redirect_uri: Redirect URI for OAuth
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        
        # Initialize client credentials flow (for app-only requests)
        client_credentials_manager = SpotifyClientCredentials(
            client_id=client_id,
            client_secret=client_secret
        )
        self.sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        
        logger.info("Spotify client initialized successfully")
    
    def search_tracks(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Search for tracks on Spotify.
        
        Args:
            query: Search query
            limit: Maximum number of results
            
        Returns:
            List of track dictionaries
        """
        try:
            results = self.sp.search(q=query, type='track', limit=limit)
            tracks = results['tracks']['items']
            
            # Simplify track data
            simplified_tracks = []
            for track in tracks:
                simplified_track = {
                    'id': track['id'],
                    'name': track['name'],
                    'artist': ', '.join([artist['name'] for artist in track['artists']]),
                    'album': track['album']['name'],
                    'popularity': track['popularity'],
                    'preview_url': track['preview_url'],
                    'external_url': track['external_urls']['spotify']
                }
                simplified_tracks.append(simplified_track)
            
            logger.info(f"Found {len(simplified_tracks)} tracks for query: {query}")
            return simplified_tracks
            
        except Exception as e:
            logger.error(f"Error searching tracks: {e}")
            return []
    
    def get_recommendations_by_mood(self, mood: str, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Get music recommendations based on mood.
        
        Args:
            mood: User's current mood
            limit: Maximum number of recommendations
            
        Returns:
            List of recommended tracks
        """
        # Define mood-based audio features
        mood_features = self._get_mood_audio_features(mood)
        
        try:
            # Add seed genres - Spotify requires at least one seed
            seed_genres = ['pop', 'rock', 'electronic', 'indie', 'alternative']
            recommendations = self.sp.recommendations(
                limit=limit,
                seed_genres=seed_genres[:1],  # Use just one seed genre
                **mood_features
            )
            
            tracks = []
            for track in recommendations['tracks']:
                track_info = {
                    'id': track['id'],
                    'name': track['name'],
                    'artist': ', '.join([artist['name'] for artist in track['artists']]),
                    'album': track['album']['name'],
                    'popularity': track['popularity'],
                    'preview_url': track['preview_url'],
                    'external_url': track['external_urls']['spotify']
                }
                tracks.append(track_info)
            
            logger.info(f"Generated {len(tracks)} recommendations for mood: {mood}")
            return tracks
            
        except Exception as e:
            logger.error(f"Error getting mood recommendations: {e}")
            # Fallback: search for mood-related tracks instead
            logger.info(f"Falling back to search for mood: {mood}")
            return self._fallback_search_by_mood(mood, limit)
    
    def _fallback_search_by_mood(self, mood: str, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Fallback method: search for tracks using mood keywords.
        
        Args:
            mood: User's mood
            limit: Maximum number of results
            
        Returns:
            List of tracks from search results
        """
        # Define search terms for each mood
        mood_search_terms = {
            'happy': 'upbeat happy energetic positive',
            'sad': 'sad melancholy emotional ballad',
            'energetic': 'energetic pump up workout motivational',
            'calm': 'chill relaxing ambient peaceful',
            'romantic': 'romantic love ballad intimate',
            'focused': 'instrumental focus study ambient'
        }
        
        search_query = mood_search_terms.get(mood.lower(), 'popular music')
        logger.info(f"Searching for: {search_query}")
        return self.search_tracks(search_query, limit)
    
    def _get_mood_audio_features(self, mood: str) -> Dict[str, float]:
        """
        Convert mood to Spotify audio features.
        
        Args:
            mood: User's mood
            
        Returns:
            Dictionary of audio features for recommendations
        """
        # Predefined mood mappings to Spotify audio features
        mood_mappings = {
            'happy': {
                'target_valence': 0.8,
                'target_energy': 0.7,
                'target_danceability': 0.7
            },
            'sad': {
                'target_valence': 0.2,
                'target_energy': 0.3,
                'target_acousticness': 0.6
            },
            'energetic': {
                'target_energy': 0.9,
                'target_danceability': 0.8,
                'target_tempo': 120
            },
            'calm': {
                'target_valence': 0.5,
                'target_energy': 0.3,
                'target_instrumentalness': 0.4
            },
            'romantic': {
                'target_valence': 0.6,
                'target_energy': 0.4,
                'target_acousticness': 0.5
            },
            'focused': {
                'target_energy': 0.5,
                'target_instrumentalness': 0.7,
                'target_valence': 0.4
            }
        }
        
        return mood_mappings.get(mood.lower(), {
            'target_valence': 0.5,
            'target_energy': 0.5
        })
    
    def get_track_details(self, track_id: str) -> Optional[Dict[str, Any]]:
        """
        Get detailed information about a specific track.
        
        Args:
            track_id: Spotify track ID
            
        Returns:
            Track details or None if not found
        """
        try:
            track = self.sp.track(track_id)
            audio_features = self.sp.audio_features([track_id])[0]
            
            return {
                'id': track['id'],
                'name': track['name'],
                'artist': ', '.join([artist['name'] for artist in track['artists']]),
                'album': track['album']['name'],
                'popularity': track['popularity'],
                'preview_url': track['preview_url'],
                'external_url': track['external_urls']['spotify'],
                'audio_features': audio_features
            }
            
        except Exception as e:
            logger.error(f"Error getting track details: {e}")
            return None