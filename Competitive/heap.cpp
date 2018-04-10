#include<iostream>
#include<vector>

namespace {

		template< typename Data >
		void swap( std::vector< Data >& heap, int p, int r ){
			Data temp = heap[p];
			heap[p] = heap[r];
			heap[r] = temp;

		}
}

template <typename Data>
class Heap final{
	public:
		Heap(){
			m_size = 0;	
			m_heap.push_back( Data() );
		}

		Heap( const Heap& heap ){

		}

		Heap& operator=( const Heap& heap ){

			return *this;
		}

		void addElement( Data element ){
			m_heap.push_back( element );
			m_size++;
				
		}

		void deleteElement( Data element ){

		}

		void printMin(){

		}

	private:
		std::vector< Data > m_heap;
		int m_size;

		void minHeapify( int index ){
			int element_index = m_size-1
			int parent_index = element_index / 2;
			if( parent_index > 0 && m_heap[m_size] < m_heap[parent_index] ){
				swap<Data>( m_heap, parent_index, element_index );
				
			}

		}

};









