import axiosInstance from './axios.instance'
import { VideoPrediction } from '../models/videosModel'

const httpOptions = {
  headers: {
    'Content-Type': 'application/json'
  }
}

export default class PredictionsService {
  private baseUrl = '/api/pred'

  getPrediction (): Promise<VideoPrediction> {
    return axiosInstance.get<VideoPrediction>(this.baseUrl)
      .then(response => response.data)
      .then((h) => {
        return h
      })
      .catch((e) => {
        console.log(e)
        return Promise.resolve({} as VideoPrediction)
      })
  }
}

// import axiosInstace from './axios.instance'

// const httpOptions = {
//   headers: {
//     'Content-Type': 'application/json'
//   }
// }

// export default class HeroService {
//   private heroesUrl = '/api/huh' // URL to web api

//   /** GET heroes from the server */
//   getHeroes (): Promise<Hero[]> {
//     return axiosInstace.get<Hero[]>(this.heroesUrl)
//       .then(response => response.data)
//       .then((h) => {
//         this.log('fetched heroes')
//         return h
//       })
//       .catch(this.handleError<Hero[]>('getHeroes', []))
//   }

//   /** GET hero by id. Return `undefined` when id not found */
//   getHeroNo404<Data> (id: number): Promise<Hero> {
//     const url = `${this.heroesUrl}/?id=${id}`
//     return axiosInstace.get<Hero[]>(url)
//       .then(responce => responce.data[0])
//       .then(h => {
//         const outcome = h ? `fetched` : `did not find`
//         this.log(`${outcome} hero id=${id}`)
//         return h
//       })
//       .catch(this.handleError<Hero>(`getHero id=${id}`))
//   }

//   /** GET hero by id. Will 404 if id not found */
//   getHero (id: number): Promise<Hero> {
//     const url = `${this.heroesUrl}/${id}`
//     return axiosInstace.get<Hero>(url)
//       .then(response => response.data)
//       .then(hero => {
//         this.log(`fetched hero id=${id}`)
//         return hero
//       })
//       .catch(this.handleError<Hero>(`getHero id=${id}`))
//   }

//   /* GET heroes whose name contains search term */
//   searchHeroes (term: string): Promise<Hero[]> {
//     if (!term.trim()) {
//       return Promise.resolve([])
//     }
//     return axiosInstace.get<Hero[]>(`${this.heroesUrl}/?name_like=${term}`)
//       .then(response => response.data)
//       .then(heroes => {
//         this.log(`found heroes matching "${term}"`)
//         return heroes
//       })
//       .catch(this.handleError<Hero[]>('searchHeroes', []))
//   }

//   /** POST: add a new hero to the server */
//   addHero (hero: HeroDraft): Promise<Hero> {
//     return axiosInstace.post<Hero>(this.heroesUrl, hero, httpOptions)
//       .then(response => response.data)
//       .then(newHero => {
//         this.log(`added hero w/ id=${newHero.id}`)
//         return newHero
//       })
//       .catch(this.handleError<Hero>('addHero'))
//   }

//   /** DELETE: delete the hero from the server */
//   deleteHero (hero: Hero | number): Promise<Hero> {
//     const id = typeof hero === 'number' ? hero : hero.id
//     const url = `${this.heroesUrl}/${id}`

//     return axiosInstace.delete<Hero>(url, httpOptions)
//       .then(_ => {
//         this.log(`deleted hero id=${id}`)
//         return hero as Hero
//       })
//       .catch(this.handleError<Hero>('deleteHero'))
//   }

//   /** PUT: update the hero on the server */
//   updateHero (hero: Hero): Promise<any> {
//     return axiosInstace.put(this.heroesUrl + `/${hero.id}/`, hero, httpOptions)
//       .then(_ => {
//         this.log(`updated hero id=${hero.id}`)
//       })
//       .catch(this.handleError<any>('updateHero'))
//   }

//   /**
//    * Handle Http operation that failed.
//    * Let the app continue.
//    * @param operation - name of the operation that failed
//    * @param result - optional value to return as the promise result
//    */
//   private handleError<T> (operation = 'operation', result?: T) {
//     return (error: any): Promise<T> => {
//       console.error(error) // log to console instead
//       this.log(`${operation} failed: ${error.message}`)
//       return Promise.resolve(result as T)
//     }
//   }

//   /** Log a HeroService message with the MessageService */
//   private log (message: string) {
//     this.messageService.add(`HeroService: ${message}`)
//   }
// }
