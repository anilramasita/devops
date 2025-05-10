resource "spotify_playlist" "Bollywood" {
  name="Bollywood"
  tracks = ["4FlytPPQPsoBQptS2CnFGZ"]
}

data "spotify_search_track" "eminem" {
  artist = "Eminem"
}
resource "spotify_playlist" "Eminem" {
  name="Eminem"
  tracks = [data.spotify_search_track.eminem.tracks[0].id,
  data.spotify_search_track.eminem.tracks[1].id,
  data.spotify_search_track.eminem.tracks[2].id]
}